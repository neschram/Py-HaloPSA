"""halo_api/core/auth.py

Contains authentication resources for the
HaloPSA API context.

"""

# python
from datetime import datetime, timedelta

# 3rd party
import requests

from halo_api.core.utils import default_headers
from halo_api.config.settings import (
    AUTH_URL,
    CLIENT_ID,
    CLIENT_SECRET,
    GRANT_TYPE,
    SCOPE,
    TENANT,
)


class HaloAuth:
    """HaloAuth

    Authentication object for the HaloPSA API as defined by
    https://haloservicedesk.com/apidoc/authentication/client
    """

    _AUTH_PARAMS: dict[str, str] = {
        "grant_type": GRANT_TYPE,
        "tenant": TENANT,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    _AUTH_URL: str = AUTH_URL
    _AUTH_HEADERS: dict[str, str] = default_headers()
    _HEADERS: dict[str, str] = default_headers()
    _LOGGED_IN: bool = False
    _EXPIRE_ON: datetime = None

    def __init__(self, **extra):
        """__init__

        Initialize a HaloPSA Authentication object.

        Args:
            **extra (dict, optional): additional object attributes

        """
        if extra:
            for k, v in extra.items():
                setattr(self, k, v)
        self.expire_on = datetime(2000, 1, 1, 0, 0, 0)

    def _authenticate(self) -> None | str:
        """authenticate

        authentication request to HaloPSA
        """
        params: dict[str, str] = self._AUTH_PARAMS
        headers: dict[str, str] = self.auth_HEADERS

        response = requests.post(
            url=self._AUTH_URL, headers=headers, data=params
        )  #: collect the _AUTH_HEADERS data from authentication

        if response.status_code == 200:  #: login successful
            data = response.json()
            self.headers = headers
            self.headers["Authorization"] = (
                f"{data['token_type']} {data['access_token']}"
            )
            self.expire_on = datetime.now() + timedelta(
                seconds=data["expires_in"]
            )
            self.logged_in: bool = True

        else:  #: return the response error
            return f"{response.status_code}: {response.reason}"

    def _is_expired(self) -> bool:
        """_is_expired

        Check that the api authentication token is valid
        """
        # don't check if the api has never authenticated
        if self.logged_in is False:
            return True
        # check the expire date is later than now
        return datetime.now() > self.expire_on

    def connect(self):
        """connect

        Checks to determine if the API is authenticated.
        If not, it calls :func:`self._authenticate()` to retrieve an active
        connection to the API endpoint.
        """
        if (self.logged_in is False) or self._is_expired():
            self._authenticate()

    def delete_header(self, header: dict[str, str]) -> None:
        """delete_header

        Remove a header from the request headers.
        """
        if header in self.headers:
            del self._HEADERS[header]

    @property
    def auth_HEADERS(self) -> dict[str, str]:
        """auth_HEADERS

        Request headers to pass when authenticating the API.

        """
        return self._AUTH_HEADERS

    @auth_HEADERS.setter
    def auth_HEADERS(self, header: dict[str, str]) -> None:
        """auth_HEADERS.setter

        Update `self._AUTH_HEADERS` with the supplied `header` information
        """
        self._AUTH_HEADERS.update(header)

    @auth_HEADERS.deleter
    def auth_HEADERS(self) -> None:
        """auth_HEADERS.deleter

        Return `self._AUTH_HEADERS` to its original state
        """
        self._AUTH_HEADERS = default_headers()

    @property
    def auth_params(self) -> dict[str, str]:
        """auth_params

        POST request query parameters for the authentication
        request.
        """
        return self._AUTH_PARAMS

    @auth_params.setter
    def auth_params(self, param: dict[str, str]) -> None:
        """auth_params.setter

        Add or update the authentication request parameter, `param`.
        """
        self._AUTH_PARAMS.update(param)

    @auth_params.deleter
    def auth_params(self) -> None:
        """auth_params.deleter

        Resets the authentication request parameters to their default state.
        """
        self._AUTH_PARAMS: dict[str, str] = {
            "grant_type": GRANT_TYPE,
            "scope": SCOPE,
            "tenant": TENANT,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        }

    @property
    def expire_on(self) -> datetime:
        """expire_on

        The datetime value for when the authentication token
        will expire.
        """
        return self._expire_on

    @expire_on.setter
    def expire_on(self, expiration: datetime) -> None:
        """expire_on.setter

        Set the datetime value of the authentication token's
        expiration.
        """
        self._expire_on = expiration

    @expire_on.deleter
    def expire_on(self) -> None:
        """expire_on.deleter

        Sets the expiration date to a time in the past.
        """
        self._expire_on = datetime(2000, 1, 1, 0, 0, 0)

    @property
    def logged_in(self) -> bool:
        """logged_in

        Expresses the validity of the current authentication state.

        Returns:
            bool: If authentication is valid (`True`) or not (`False`)
        """
        return self._LOGGED_IN

    @logged_in.setter
    def logged_in(self, val: bool) -> None:
        """logged_in.setter

        Sets the value of `self._LOGGED_IN` to `val`.
        """
        self._LOGGED_IN = val

    @logged_in.deleter
    def logged_in(self) -> None:
        """logged_in.deleter

        Do not delete the variable, instead set it to `False`.
        """
        self.logged_in = False
