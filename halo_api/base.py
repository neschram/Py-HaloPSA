import json
from datetime import datetime, timedelta
from requests import request
from .settings import (
    AUTH_URL,
    RESOURCE_SERVER,
    TENANT,
    CLIENT_ID,
    CLIENT_SECRET,
    GRANT_TYPE,
    CONTENT_TYPE,
    SCOPE,
)
from .halo_properties import Client, Agent, Ticket


class HaloApi:
    """HaloAip

    Manages the API call to HaloPSA

    Raises:
        ValueError: login response errored
    """

    _tenant: str = TENANT
    _auth_url: str = AUTH_URL
    _action_url: str = RESOURCE_SERVER
    _client: str = CLIENT_ID
    _secret: str = CLIENT_SECRET
    _grant_type: str = GRANT_TYPE
    _scope: str = SCOPE
    _content_type: str = CONTENT_TYPE
    _auth_header: str = f"Bearer {_secret}"

    def _authenticate(self):
        """authenticate

        authentication request to HaloPSA
        """
        payload_data: list[str] = [
            f"grant_type={self.grant_type}",
            f"scope={self.scope}",
            f"tenant={self.tenant}",
            f"client_id={self.client}",
            f"client_secret={self.secret}",
        ]  #: request data

        headers: dict = {
            "Content-Type": self.content_type,
            "Authorization": self.auth_header,
        }  #: request headers

        payload = "&".join(payload_data)  #: login does not support json

        response = request(
            "POST",
            self.auth_url,
            headers=headers,
            data=payload,
        )  #: collect the response data from authentication

        if response.status_code == 200:  #: login successful
            data = json.loads(response.text)
            self.token: str = data["access_token"]
            self.token_type: str = data["token_type"]
            self.token_header: str = f"{self.token_type} {self.token}"
            self.expire_on = datetime.now() + timedelta(
                seconds=data["expires_in"]
            )
            self.logged_in: bool = True

        else:  #: return the response error
            self.msg = f"{response.status_code}: {response.reason}"

    def _is_expired(self) -> bool:
        """_is_expired

        Check that the api authentication token is valid
        """
        # don't check if the api has never authenticated
        if self.logged_in is False:
            return True
        # check the expire date is later than now
        return datetime.now() > self.expire_on

    def __init__(
        self,
        tenant: str = _tenant,
        auth_url: str = _auth_url,
        action_url: str = _action_url,
        client: str = _client,
        secret: str = _secret,
        grant_type: str = _grant_type,
        scope: str = _scope,
        content_type: str = _content_type,
        auth_header: str = _auth_header,
    ):
        """__init__

        Initialize the call manager

        Args:
            auth_url (str, optional): HaloPSA authentication url.
            Defaults to _auth_url.
            action_url (str, optional): HaloPSA resource server url.
            Defaults to _action_url.
            client (str, optional): API Client ID. Defaults to _client.
            secret (str, optional): API Client Secret. Defaults to _secret.
            grant_type (str, optional): API parameter "grant_type".
            Defaults to _grant_type.
            scope (str, optional): API parameter "scope". Defaults to _scope.
            content_type (str, optional): API Header "Content-Type".
            Defaults to _content_type.
            auth_header (str, optional): API Header "Authorization".
            Defaults to _auth_header.
        """
        self.tenant = tenant
        self.auth_url = auth_url
        self.action_url = action_url
        self.client = client
        self.secret = secret
        self.grant_type = grant_type
        self.scope = scope
        self.content_type = content_type
        self.auth_header = auth_header
        self.logged_in = False
        self._authenticate()

    def check_status(self):
        if (self.logged_in is False) or self._is_expired():
            self._authenticate()

    @property
    def clients(self) -> dict[str, str]:
        self.check_status()
        return Client(token=self.token_header)

    @property
    def agents(self) -> dict[str, str]:
        self.check_status()
        return Agent(token=self.token_header)

    @property
    def tickets(self) -> dict[str, str]:
        self.check_status()
        return Ticket(token=self.token_header)
