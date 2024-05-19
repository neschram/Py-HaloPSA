# halo_api/core/auth.py

# python
from datetime import datetime, timedelta

# 3rd party
import requests

# local
from .settings import (
    AUTH_URL,
    CLIENT_ID,
    CLIENT_SECRET,
    CONTENT_TYPE,
    GRANT_TYPE,
    SCOPE,
    TENANT,
)


class HaloAuth:
    """HaloAuth

    Authentication object for the HaloPSA API as defined by
    https://haloservicedesk.com/apidoc/authentication/client

    Properties:
        auth_headers (dict[str, str]): Authentication request headers
        headers (dict[str, str]): Query request headres
        auth_params (dict[str, str]): Http query parameters
        expire_on (str): Expiration date of an auth token
        logged_in (bool): Signifies that HaloAuth has an active auth token

    Methods:
        :func:`_authenticate()`: authenticate and set an access token
        :func:`_is_expired()`: verify if authentication is active
        :func:`connect()`: authenticate only if not active
    """

    _auth_params: dict[str, str] = {
        "grant_type": GRANT_TYPE,
        "tenant": TENANT,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    _auth_url: str = AUTH_URL
    _content_header: dict[str, str] = {"Content-Type": CONTENT_TYPE}
    _auth_headers: dict[str, str] = _content_header.copy()
    _headers: dict[str, str] = _content_header.copy()
    _logged_in: bool = False
    _expire_on: datetime = None

    @property
    def auth_headers(self) -> dict[str, str]:
        """auth_headers

        Request headers to pass when authenticating the API
        """
        return self._auth_headers

    @auth_headers.setter
    def auth_headers(self, header: dict[str, str]) -> None:
        """auth_headers.setter

        Update `self._auth_headers` with the supplied `header` information
        """
        self._auth_headers.update(header)

    @auth_headers.deleter
    def auth_headers(self) -> None:
        """auth_headers.deleter

        Return `self._auth_headers` to its original state
        """
        self._auth_headers = self._content_header.copy()

    @property
    def headers(self) -> dict[str, str]:
        """headers

        Request headers for an API call
        """
        return self._headers

    @headers.setter
    def headers(self, header: dict[str, str]) -> None:
        """headers.setter

        Update the request headers with the provided `header`.
        """

        self._headers.update(header)

    def delete_header(self, header: dict[str, str]) -> None:
        """delete_header

        Remove a header from the request headers.
        """
        if header in self.headers:
            del self._headers[header]

    @property
    def auth_params(self) -> dict[str, str]:
        """auth_params

        POST request query parameters for the authentication
        request.
        """
        return self._auth_params

    @auth_params.setter
    def auth_params(self, param: dict[str, str]) -> None:
        """auth_params.setter

        Add or update the authentication request parameter, `param`.
        """
        self._auth_params.update(param)

    @auth_params.deleter
    def auth_params(self) -> None:
        """auth_params.deleter

        Resets the authentication request parameters to their default state.
        """
        self._auth_params: dict[str, str] = {
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

    def __init__(self, **extra):
        """HaloAuth

        Authentication object for the HaloPSA API

        Properties:
            auth_headers (dict[str, str]): Authentication request headers
            headers (dict[str, str]): Query request headres
            auth_params (dict[str, str]): Http query parameters
            expire_on (str): Expiration date of an auth token
            logged_in (bool): Signifies that HaloAuth has an active auth token

        Methods:
            :func:`_authenticate()`: authenticate and set an access token
            :func:`_is_expired()`: verify if authentication is active
            :func:`connect()`: authenticate only if not active
        """
        if extra:
            for k, v in extra.items():
                setattr(self, k, v)
        self.expire_on = datetime(2000, 1, 1, 0, 0, 0)

    def _authenticate(self) -> None | str:
        """authenticate

        authentication request to HaloPSA
        """
        params: dict[str, str] = self._auth_params
        headers: dict[str, str] = self.auth_headers

        response = requests.post(
            url=self._auth_url, headers=headers, data=params
        )  #: collect the response data from authentication

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
