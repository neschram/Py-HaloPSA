from datetime import datetime, timedelta
from requests import Response
from typing import Any
# 3rd party


# Py-HaloPSA
from halo_psa.settings import (
    AUTH_URL,
    CLIENT_ID,
    CLIENT_SECRET,
    CONTENT_TYPE,
    GRANT_TYPE,
    SCOPE,
    TENANT,
)

# Local
from .utils import POST
from .exceptions import ResponseError

AUTH_PARAMS: dict[str, str] = {
    "grant_type": GRANT_TYPE,
    "tenant": TENANT,
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "scope": SCOPE,
}
"""Authentication parameters for authorizing the package against
    Your HaloPSA API endpoint.
"""
BASE_HEADER: dict[str, str] = {"Content-Type": CONTENT_TYPE}
"""The initial header required for all API calls.
    BASE_HEADER only contains the Content-Type header.
"""


class Auth:
    """Auth

    An object for managing authentication to your
    custom HaloPSA API.

    Attrs:
        page (str): Authentication URL
        auth_params (dict[str, str]): Parameters to send for an auth request.
        auth_headers (dict[str, str]): Headers for an authentication request.
        auth_credentials (dict[str, str]): Authorization credentials
        created after sending a POST request to the authentication endpoint.

    """

    def __init__(self, page: str = AUTH_URL, **kwargs) -> None:
        """Auth.__init__

        Initialize an instance of Auth with the provided arguments.

        Args:
            grant (str): Grant Type
            tenant (str): Tenant Name
            client (str): Client ID
            secret (str): Client Secret
            scope (str): Scope of Authorization
            url (str): Authentication URL
            credentials (dict[str,str]): Authorization credentials

        """

        # set the base Auth data
        self.page: str = page
        self.expire_on: datetime = datetime.now()
        self.auth_params: dict[str, str] = AUTH_PARAMS
        self.auth_headers: dict[str, str] = BASE_HEADER
        self.auth_credentials: dict[str, str] = dict()

        # Apply additional kwargs
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def _is_valid(self) -> bool:
        """_is_valid

        Checks `self.expire_on` is greater than
        the current time.

        Returns:
            bool: `self.expire_on > datetime.now()`
        """
        return self.expire_on > datetime.now()

    def _authenticate(self) -> str | None:
        """_authenticate

        Authenticate against your HaloPSA API endpoint.

        Returns:
            str | None: Authentication context
        """
        req_dt: datetime = datetime.now()
        req: POST = POST(
            url=self.page, headers=self.auth_headers, data=self.auth_params
        )
        resp: Response = req()
        """Response context from the Authentication POST request."""

        if resp.status_code == 200:  #: login successful
            data: dict[str, Any] = resp.json()
            self.expire_on: datetime = req_dt - timedelta(
                seconds=data["expires_in"],
            )
            self.auth_credentials: dict[str, str] = {
                "Authorization": f"{data['token_type']} {data['access_token']}"
            }
        else:  #: return the response error
            raise ResponseError(
                f"{resp.status_code}: {resp.reason}",
                f"url: {resp.url}",
                f"headers: {resp.request.headers}",
                f"method: {resp.request.method}",
                "request [url, headers, data]: [{0}, {1}, {2}]".format(
                    self.page, self.auth_headers, self.auth_params
                ),
            )

    def connect(self) -> None:
        """connect

        Checks that there is currently a valid authorization context.
        If not, call :func:`_authenticate()` to create one.
        """
        if not self._is_valid():
            self._authenticate()

    @property
    def logged_in(self) -> bool:
        """logged_in

        A convenient way of accessing the return value of \
            :func:`self._is_valid()`

        """
        return self._is_valid()

    @property
    def credentials(self) -> dict[str, str]:
        """credentials

        Get authentication credentials,

        Returns:
            dict[str, str]: _description_
        """
        self.connect()
        return self.auth_credentials
