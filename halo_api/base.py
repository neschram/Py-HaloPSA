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
    RESOURCE_SERVER,
    SCOPE,
    TENANT,
)


class Get:
    """Performs the task of sending an API GET Request
    to HaloPSA's API interface.

    Fields:
        page (str): the url of the API request page
        list_value (str): name of the field storing data in the response
        params (dict[str, str]): query parameters to pass in the request
        headers (dict[str, str]): http headers to pass in the request

    Methods:
        :func:`_all()`: query the Resource for all instances
        :func:`_get_by_id(pk: int)`: query the Resource for a single instance
        from the supplied instance id (`pk`)
        :func:`get(pk: list[int] | int)`: returns a dictionary of items
        returned by a GET request to the API endpoint
    """

    _page: str = None
    _list_value: str = None
    _params: dict[str, str] = None
    _headers: dict[str, str] = None

    def __init__(
        self,
        page: str = _page,
        list_value: str = _list_value,
        params: dict[str, str] = _params,
        headers: dict[str, str] = _headers,
    ) -> None:
        """GET

        Performs the task of sending an API GET Request
        to HaloPSA's API interface.

        Args:
            page (_type_): url of the API request page
            list_value (_type_): name of the content field in the response
            params (_type_): query parameters to pass in the request
            headers (_type_): http headers to pass in the request


        Methods:
            :func:`_all()`: query the Resource for all instances
            :func:`_get_by_id(pk: int)`: query the Resource for
            a single instance from the supplied instance id (`pk`)
            :func:`get(pk: list[int] | int)`: returns a dictionary of
            items returned by a GET request to the API endpoint
        """
        self.page = page
        self.list_value = list_value
        self.params = params
        self.headers = headers

    def _all(self):
        """all

        Query the Resource for data on all instances available
        """
        return requests.get(
            url=self.page, headers=self.headers, data=self.params
        ).json()[self.list_value]

    def _get_by_id(self, pk: int) -> dict:
        """get

        Query the Resource for data on a single instance by its id
        """
        return requests.get(
            url=f"{self.page}/{pk}", headers=self.headers, data=self.params
        ).json()

    def get(self, items: list[int] | int = None) -> dict:
        """get

        Request one or more Resource instances.

        Args:
            items (list[int] | int, optional): one or more id's for the lookup.
            Defaults to None.

        Returns:
            dict: {instance id: instance} for each returned Resource instance
        """
        if items is not None:
            if type(items) is int:
                return {items: self._get_by_id(items)}
            if type(items) is list:
                return {i: self._get_by_id(i) for i in items}
        return {obj["id"]: obj for obj in self._all()}


class HaloAuth:
    """HaloAuth

    Authentication object for the HaloPSA API

    Properties:
        headers (dict[str, str]): Http request headers
        auth_params (dict[str, str]): Http query parameters
        logged_in (bool): signifies that HaloAuth has authenticated

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
        If not, it calls :func:`self._authenticate()` to retrieve an active
        connection to the API endpoint.
        """
        if (self.logged_in is False) or self._is_expired():
            self._authenticate()


class ResourceItem:

    _FIELDS: list = []
    _TITLE: str = "name"

    def __init__(self, data: dict, title: str = _TITLE) -> "ResourceItem":
        self._title: str = title
        for k, v in data.items():
            if k not in self.fields:
                self.fields = k
            setattr(self, k, v or "None")

    def get(self, field: str):
        if field in self.fields:
            return getattr(self, field)
        return NameError(
            field, f"not found, available options are {self.fields}"
        )

    @property
    def fields(self) -> list:
        return self._FIELDS

    @fields.setter
    def fields(self, item) -> property:
        self._FIELDS.append(item)

    @property
    def title(self) -> str:
        """title

        String identification of the instance.
        Defaults to `"name"`.

        Returns:
            str: self._title
        """
        return self._title

    @title.setter
    def title(self, t: str) -> None:
        """title.setter

        Sets the instances `_title` value.

        Args:
            t (str): title
        """
        self._title = t

    @title.deleter
    def title(self) -> None:
        """title.deleter

        Sets `self._title` to the default `self._TITLE` value.
        """
        self._title = self._TITLE

    def __str__(self) -> str:
        return f"{self.id}: {self.title}"


class HaloResource(HaloAuth):
    _action_url: str = RESOURCE_SERVER
    _params: dict[str, str] = {"pageinate": False}
    _page_name: str = None
    _list_value: str = None
    _OBJECTS: dict[int, "ResourceItem"] = None

    @property
    def action_url(self) -> str:
        """action_url

        Resource server url
        """
        return self._action_url

    @property
    def params(self) -> dict[str, str]:
        """params

        GET request query parameters
        """
        return self._params

    @params.setter
    def params(self, param: dict[str, str]) -> None:
        """params.setter

        Updates the existing data in `self._params` instead of
        overwriting the entire dictionary.
        """
        self._params.update(param)

    @params.deleter
    def params(self) -> None:
        """params.deleter

        Set params to an empty dictionary
        """
        self.params: dict[str, str] = {}

    @property
    def page_name(self) -> str:
        """page_name

        API page name for the Resource. Stored as `self._page_name`.
        """
        return self._page_name

    @page_name.setter
    def page_name(self, page: str) -> None:
        """page_name.setter

        Assigns the value of `page` to `self._page_name`.
        """
        self._page_name = page

    @property
    def list_value(self) -> str:
        """list_value

        Typically, the lowercased value of `page_name`,
        `list_value` is the response content section that stores our
        desired data.
        """
        return self._list_value

    @list_value.setter
    def list_value(self, val: str) -> property:
        """list_value.setter

        Assigns the value of `val` to `self._list_value`.
        """
        self._list_value = val

    @property
    def page_link(self) -> str:
        """page_link

        Combines `action_url` and `page_name` to form the full
        url to the Resource's GET endpoint.

        Returns:
            str: "`self.action_url`/`self.page_name`"
        """
        return f"{self.action_url}/{self.page_name}"

    def _build(self):
        """_build

        Authenticate to the API endpoint, then build out a list of
        available objects.
        """
        self.connect()
        data = self.GET.get()
        for obj in iter(data):
            item = ResourceItem(obj)
            self._OBJECTS.update({item.id: item})

    def __init__(self, build_on_init: bool = False, **extra):
        """HaloResource

        An API endpoint or "Resource" as defined by the HaloPSA API

        Args:
            `build_on_init` (bool, optional): calls `self._build()` on instance
            initialization if `True`. Defaults to `False`.
        """
        super().__init__(**extra)
        self._OBJECTS = {}
        self.GET = Get(
            page=self.page_link,
            list_value=self.list_value,
            params=self.params,
            headers=self.headers,
        )
        if build_on_init:
            self._build()

    def list_all(self) -> list[str]:
        """list_all

        List all known Resource instances.
        """
        return [str(v) for v in self._OBJECTS.values()]

    def get(self, items: list[int] | int = None) -> dict:
        """get

        Retrieve one or more instances of the Resource.

        Args:
            items (list[int] | int, optional): one or more ids to look up.
            Defaults to None.

        Returns:
            dict: found Resource instances
        """
        # return variable dataset
        dataset: dict = dict()
        # id(s) were provided
        if items is not None:  #: if we're looking for specific ids
            if type(items) is list:  #: if there's more than one id
                lookup: list = list()  #: store id's that we haven't seen
                for i in iter(items):
                    try:  #: get the item if we've seen it previously
                        dataset.update(self._OBJECTS[i])
                    except KeyError:  #: add unfound ids to the lookup list
                        lookup.append(i)
                new_items: dict = self.GET.get(
                    lookup
                )  #: find the unknown items
                dataset.update(
                    {i["id"]: i for i in new_items}
                )  #: add the items to the return dict
            try:  #: if there is only one id see if it's a known item
                dataset.update({i: self._OBJECTS[i]})
            except KeyError:  #: if it is not known, retrieve it from the API
                new_item = self.GET.get(items)
                self._OBJECTS[items] = new_item  #: store the new item
                dataset[items] = new_item  #: add the item to the return dict
        # no ids were provided, place an API call to retrieve all items
        dataset = self.GET.get()
        self._OBJECTS.update(
            {i["id"]: i for i in dataset}
        )  #: store the found items
        return dataset
