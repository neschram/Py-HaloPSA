from typing import Any
from requests import Response, post
from datetime import datetime, timedelta
from .utils import ValidateAuthToken, TokenExpired
from halopsa.config import settings
from halopsa.core import BaseData
from halopsa.core.validators import check_response

CONTENT_HEADER: BaseData = BaseData({"Content-Type": settings.CONTENT_TYPE})
AUTH_PARAMS: BaseData = BaseData(
    grant_type=settings.GRANT_TYPE,
    tenant=settings.TENANT,
    client_id=settings.CLIENT_ID,
    client_secret=settings.CLIENT_SECRET,
    scope=settings.SCOPE,
)
EXPIRES: datetime = datetime(2000, 1, 1, 0, 0, 1)
TOKEN_TYPE: str = "Bearer"
ACCESS_TOKEN: str = ""


class AuthToken(BaseData):

    # Attribute placeholders
    expires: datetime = ...
    token_type: str = ...
    access_token: str = ...

    # data dict for instanciating a raw AuthToken
    _BASE_DATA: dict[str, any] = {
        "expires": EXPIRES,
        "token_type": TOKEN_TYPE,
        "access_token": ACCESS_TOKEN,
    }

    def __init__(self, data: dict[str, Any] = _BASE_DATA, **kwds) -> None:
        super().__init__(data, **kwds)

    def __call__(self) -> dict[str, str]:
        """__call__

        Return a formatted HaloPSA authorization.

        Returns:
            dict[str, str]: {"Authorization": str(self)}
        """
        return {"Authorization": str(self)}

    def __str__(self) -> str:
        """__str__

        The string representation of an AuthToken instance.

        Returns:
            str: `f"{self.token_type} {self.token}"`
        """
        f"{self.token_type} {self.token}"

    def is_valid(self) -> bool:
        """is_valid

        Returns a boolean dependent on validation of the token
        throwing a :class:`TokenExpired` exception.

        Returns:
            bool:   `True` if an exception is not caught.
                    `False` if an exception is caught.

        """
        try:
            ValidateAuthToken(self.expires)
            return True
        except TokenExpired:
            return False

    def build(
        self, expires: datetime, token_type: str, access_token: str
    ) -> None:
        """build

        Reinitialize the AuthToken instance with new data

        Args:
            expires (datetime): the token's expiration date
            token_type (str): Type of access token
            access_token (str): Actual access token

        """
        new_token: dict[str, datetime | str] = {
            "expires": expires,
            "token_type": token_type,
            "access_token": access_token,
        }
        self.__init__(data=new_token)


class Auth:
    """A container for the HaloPSA authentication context."""

    def __init__(self, **kwds) -> None:
        """__init__
        Initialize an Auth instance

        """
        self.page: str = settings.API_URL
        """str: The HaloPSA API authentication URL"""
        self.token: AuthToken = AuthToken()
        """AuthToken: The authentication token required for requests to
        HaloPSA API Resources and their records."""
        self.auth_headers: BaseData = CONTENT_HEADER
        """BaseData: Headers required for the authentication POST request."""
        self.auth_params: BaseData = AUTH_PARAMS
        """BaseData: POST data for the HaloPSA API authentication request"""
        if kwds:
            for k, v in kwds.items():
                setattr(self, k, v)

    def _authenticate(self) -> str | None:
        """authenticate

        Builds an :class:`AuthToken` using the response data of
        a HaloPSA API authentication POST request.
        """
        req_dt: datetime = datetime.now()
        """datetime: The datetime value of the authentication POST request."""
        response: Response = post(
            url=self.page,
            headers=self.auth_headers,
            data=self.auth_params,
        )  #: response data from the authentication POST request.
        check_response(response)
        r_data: dict[str, any] = response.json()
        """dict[str, any]: Returned data from the request's response"""
        expiration: datetime = req_dt + timedelta(seconds=r_data["expires_in"])
        """datetime: expiration datetime of the authentication token"""
        # set the authentication token
        self.token.build(
            expires=expiration,
            token_type=r_data["token_type"],
            access_token=r_data["access_token"],
        )

    def _is_expired(self) -> bool:
        """_is_expired

        Checks that the autentication token is not expired.
        """
        return self.token.is_valid()

    def connect(self) -> None:
        """connect

        Validate the current authentication token before
        sending a POST request to the API's authentication endpoint.
        """
        try:
            ValidateAuthToken(self.token.expires)
        except TokenExpired:
            self._authenticate()
