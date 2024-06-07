from datetime import datetime, timedelta

# 3rd party
import requests


# Py-HaloPSA
from halo_psa.config import settings
from halo_psa.core import BaseData

_AUTH_URL = settings.AUTH_URL
_CLIENT_ID = settings.CLIENT_ID
_CLIENT_SECRET = settings.CLIENT_SECRET
_CONTENT_TYPE = settings.CONTENT_TYPE
_GRANT_TYPE = settings.GRANT_TYPE
_SCOPE = settings.SCOPE
_TENANT = settings.TENANT


class HaloAuth:
    """HaloAuth

    Authentication object for the HaloPSA API as defined by
    https://haloservicedesk.com/apidoc/authentication/client

    """

    # Default Attributes

    _CONTENT_HEADER: dict[str, str] = {"Content-Type": _CONTENT_TYPE}
    """HaloPSA required Content-Type header"""

    _AUTH_URL: str = _AUTH_URL
    """HaloPSA API authentication web address"""

    _AUTH_HEADERS: BaseData = BaseData(_CONTENT_HEADER)
    """Authentication request headers"""

    _QUERY_HEADERS: BaseData = BaseData(_CONTENT_HEADER)
    """Query request headers"""

    _AUTH_PARAMS: BaseData = BaseData(
        grant_type=_GRANT_TYPE,
        tenant=_TENANT,
        client_id=_CLIENT_ID,
        client_secret=_CLIENT_SECRET,
        scope=_SCOPE,
    )
    """Http query parameters"""

    _EXPIRE_ON: datetime = datetime(2000, 1, 1, 0, 0, 0)
    """Expiration date of an auth token"""

    _LOGGED_IN: bool = False
    """Signifies that HaloAuth has an active auth token"""

    def __init__(
        self,
        auth_url: str = _AUTH_URL,
        auth_headers: BaseData = _AUTH_HEADERS,
        headers: BaseData = _QUERY_HEADERS,
        auth_params: BaseData = _AUTH_PARAMS,
        expire_on: datetime = _EXPIRE_ON,
        logged_in: bool = _LOGGED_IN,
        **extra,
    ):
        """__init__

        Initialize the authentication class.

        Args:
            auth_url (str): HaloPSA API authentication web address.
            Defaults to _AUTH_URL.
            auth_headers (dict[str, str], optional): Authentication request
            headers. Defaults to _AUTH_HEADERS.
            headers (dict[str, str], optional): Query request headers.
            Defaults to _QUERY_HEADERS.
            auth_params (dict[str, str], optional): Http query parameters.
            Defaults to _AUTH_PARAMS.
            expire_on (datetime, optional): Expiration date of an auth token.
            Defaults to _EXPIRE_ON.
            logged_in (bool, optional): Signifies that HaloAuth has an active
            auth token. Defaults to _LOGGED_IN.
        """

        # set initial attributes
        self._auth_url = auth_url
        self._auth_headers = auth_headers
        self._query_headers = headers
        self._auth_params = auth_params
        self._expire_on = expire_on
        self._logged_in = logged_in

        if extra:
            for k, v in extra.items():
                setattr(self, k, v)

    def _authenticate(self) -> None | str:
        """authenticate

        authentication request to HaloPSA
        """
        params: dict[str, str] = self.auth_params
        headers: dict[str, str] = self.auth_headers

        response = requests.post(
            url=self.auth_url, headers=headers, data=params
        )  #: collect the response data from authentication

        if response.status_code == 200:  #: login successful
            data = response.json()
            self.query_headers = {
                "Authorization": f"{data['token_type']} {data['access_token']}",
            }
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

    @property
    def auth_url(self) -> str:
        """auth_url

        HaloPSA API authentication web address
        """
        return self._auth_url

    @property
    def auth_headers(self) -> dict[str, str]:
        """auth_headers

        Request headers to pass when authenticating the API
        """
        return self._auth_headers()

    @auth_headers.setter
    def auth_headers(self, headers: dict[str, str]) -> None:
        """auth_headers.setter

        Update `self._auth_headers` with the supplied information
        """
        for k, v in headers.items():
            self._auth_headers.add(k, v)

    @auth_headers.deleter
    def auth_headers(self) -> None:
        """auth_headers.deleter

        Return `self._auth_headers` to its original state
        """
        self._auth_headers = HaloAuth._AUTH_HEADERS().copy()

    @property
    def query_headers(self) -> dict[str, str]:
        """query_headers

        Request headers for an API call
        """
        return self._query_headers()

    @query_headers.setter
    def query_headers(self, headers: dict[str, str]) -> None:
        """query_headers.setter

        Update the request headers with the provided information.
        """
        for k, v in headers.items():
            self._query_headers.add(k, v)

    @property
    def auth_params(self) -> dict[str, str]:
        """auth_params

        POST request query parameters for the authentication
        request.
        """
        return self._auth_params()

    @auth_params.setter
    def auth_params(self, params: dict[str, str]) -> None:
        """auth_params.setter

        Add or update the authentication request parameter, `param`.
        """
        for k, v in params:
            self._auth_params.add(k, v)

    @auth_params.deleter
    def auth_params(self) -> None:
        """auth_params.deleter

        Resets the authentication request parameters to their default state.
        """
        self._auth_params: BaseData = HaloAuth._AUTH_PARAMS().copy()

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
        return self._logged_in

    @logged_in.setter
    def logged_in(self, val: bool) -> None:
        """logged_in.setter

        Sets the value of `self._logged_in` to `val`.
        """
        self._logged_in = val

    @logged_in.deleter
    def logged_in(self) -> None:
        """logged_in.deleter

        Do not delete the variable, instead set it to `False`.
        """
        self.logged_in = False
