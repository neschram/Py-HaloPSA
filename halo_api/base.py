import requests
from datetime import datetime, timedelta
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


class GET:
    page: str = None
    list_value: str = None
    params: dict[str, str] = None
    headers: dict[str, str] = None

    def __init__(self, page, list_value, params, headers) -> None:
        self.page = page
        self.list_value = list_value
        self.params = params
        self.headers = headers

    def all(self):
        return requests.get(url=self.page, headers=self.headers).json()[
            self.list_value
        ]

    def get(self, pk) -> dict:
        return requests.get(
            url=f"{self.page}/{pk}", headers=self.headers
        ).json()


class HaloAuth:
    """HaloAuth

    Authentication object for the HaloPSA API

    Properties:
        headers (dict[str, str]): Http request headers
        auth_params (dict[str, str]): Http query parameters
        logged_in (bool): signifies that HaloAuth has authenticated
    """

    _auth_params: dict[str, str] = {
        "grant_type": GRANT_TYPE,
        "tenant": TENANT,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    _auth_url: str = AUTH_URL
    _content_header: dict = {"Content-Type": CONTENT_TYPE}
    _headers: dict[str, str] = _content_header.copy()
    _logged_in: bool = False
    _expire_on: datetime = None

    @property
    def headers(self) -> dict[str, str]:
        return self._headers

    @headers.setter
    def headers(self, header: dict[str, str]) -> None:
        self._headers.update(header)

    @headers.deleter
    def headers(self) -> None:
        self._headers = self._content_header.copy()

    @property
    def auth_params(self) -> dict[str, str]:
        return self._auth_params

    @auth_params.setter
    def auth_params(self, param: dict[str, str]) -> None:
        self._auth_params.update(param)

    @auth_params.deleter
    def auth_params(self) -> None:
        self._auth_params: dict[str, str] = {
            "grant_type": GRANT_TYPE,
            "scope": SCOPE,
            "tenant": TENANT,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        }

    @property
    def expire_on(self) -> datetime:
        return self._expire_on

    @expire_on.setter
    def expire_on(self, expiration: datetime) -> None:
        self._expire_on = expiration

    @expire_on.deleter
    def expire_on(self) -> None:
        self._expire_on = datetime.now() - timedelta(days=1)

    @property
    def logged_in(self) -> bool:
        return self._logged_in

    @logged_in.setter
    def logged_in(self, val: bool) -> None:
        self._logged_in = val

    def _authenticate(self) -> None | str:
        """authenticate

        authentication request to HaloPSA
        """
        params: dict[str, str] = self._auth_params
        headers: dict[str, str] = self.headers

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

    def __init__(self, **extra):
        if extra:
            for k, v in extra.items():
                setattr(self, k, v)
        self.expire_on = datetime.now() - timedelta(days=1)

    def connect(self):
        """connect

        Checks to determine if the API is authenticated.
        If not, it calls self._authenticate() to retrieve an active
        connection to the api endpoint.
        """
        if (self.logged_in is False) or self._is_expired():
            self._authenticate()


class HaloResource(HaloAuth):
    _action_url: str = RESOURCE_SERVER
    _params: dict[str, str] = {"pageinate": False}
    _page_name: str = None
    _list_value: str = None
    _OBJECTS: dict[int, "ResourceItem"] = None

    class ResourceItem:

        _item_fields: list = []

        def __init__(self, data: dict):
            self._item_fields = []
            for k, v in data.items():
                if k not in self.fields:
                    self.fields = k
                setattr(self, k, v or "None")

        def get(self, item):
            if item in self._item_fields:
                return getattr(self, item)

        @property
        def fields(self) -> list:
            return self._item_fields

        @fields.setter
        def fields(self, item) -> None:
            self._item_fields.append(item)

        def __str__(self) -> str:
            if "name" in self.fields:
                return f"{self.id}: {self.name}"
            return f"{self.id}"

    @property
    def action_url(self) -> str:
        return self._action_url

    @property
    def params(self) -> dict[str, str]:
        return self._params

    @params.setter
    def params(self, param: dict[str, str]) -> None:
        self._params.update(param)

    @params.deleter
    def params(self) -> None:
        self.params: dict[str, str] = {}

    @property
    def page_name(self) -> str:
        return self._page_name

    @page_name.setter
    def page_name(self, page: str) -> None:
        self._page_name = page

    @property
    def list_value(self) -> str:
        return self._list_value

    @list_value.setter
    def list_value(self, val: str) -> None:
        self._list_value = val

    @property
    def page_link(self) -> str:
        return f"{self.action_url}/{self.page_name}"

    def _build(self):
        """_build

        Authenticate to the API endpoint, then build out a list of
        available objects.
        """
        self.connect()
        data = GET(
            self.page_link, self.list_value, self.params, self.headers
        ).all()
        for obj in iter(data):
            item = self.ResourceItem(obj)
            self._OBJECTS.update({item.id: item})

    def __init__(self, build_on_init: bool = False, **extra):
        super().__init__(**extra)
        self._OBJECTS = {}
        if build_on_init:
            self._build()

    def list_all(self):
        return [str(v) for v in self._OBJECTS.values()]
