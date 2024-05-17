# halo_api/halo_properties.py


import json
from requests import request
from .settings import CONTENT_TYPE, RESOURCE_SERVER


class HaloResource:
    """HaloResource

    HaloPSA defines each section of the API as a Resource.

    The :class:`HaloResource` object is a base class for each API
    resource. It sets default methods and properties that are required
    or helpful in each of the Resource objects defined later.

    Methods:

        :func:`_build_params()`
        :func:`_decode_response()`
        :func:`_list_all()`
        :func:`_find()`
        :func:`_build_headers()`
        :func:`_get_raw_data()`
        :func:`get_all()`
        :func:`get()`

    Properties:

        :func:`all`: easy way of calling :func:`_list_all()`
    """

    def __init__(
        self,
        token: str,
        page: str,
        list_value: str,
        content_type: str = CONTENT_TYPE,
        params: dict[str, str] = dict(),
    ) -> None:
        """__init__

        Args:
            token (str): API authentication token
            page (str): url for the request call
            list_value (str): used in searching the raw response for data
            content_type (str, optional): Content-Type header value.
            Defaults to CONTENT_TYPE.
            params (dict[str, str], optional): query parameters for the call.
            Defaults to dict().
        """
        self.token = token
        self.page_url: str = f"{RESOURCE_SERVER}/{page}"
        self.parameters: dict[str, str] = params or dict()
        self.content_type: str = content_type
        self.list_value = list_value

    @staticmethod
    def _build_params(params: dict[str, str]) -> str:
        """_build_params

        Given a dictionary of parameters, return a single string to pass
        in the reuqest.

        Args:
        params (dict[str,str]): a dictionary of parameters to pass in the
        API call

        Returns:
            str: all parameters joined by an ampersand (&)

        Example::
            >>> from halo_properties.py import HaloResource
            >>> parameters = {"test": "this", "method": "works"}
            >>> HaloResource._build_params(parameters)
            'test=this&method=works'
        """
        param_list: list = [f"{k}={v}" for k, v in params.items()]
        return "&".join(param_list)

    @staticmethod
    def _decode_response(response):
        """_decode_response

        Creates a python dictionary from the response text.

        If there is an error in the call, raise a ValueError citing
        the stauts code and reason.
        """
        if response.status_code == 200:  #: check for success
            return json.loads(response.text)
        raise ValueError(f"{response.status_code}: {response.reason}")

    def _list_all(self, title: str = "name"):
        """_list_all

        List all available items

        Args:
            title (str, optional): an identifying value to collect
            as the name of the item. Defaults to "name".

        Returns:
            list: ["{id} - {title}" for all items]
        """
        objs: list[dict] = self.get_all()
        if type(objs) is dict:
            objs = objs[self.list_value]
        listed_objs: list[str] = [f"{i['id']} - {i[title]}" for i in objs]
        return listed_objs

    def _find(self, item: str) -> int:
        """_find

        Look for an id to the given item

        Args:
            item (str): idenifying text for the lookup

        Raises:
            NameError: No items found

        Returns:
            int: The id of the found item.
        """
        for i in self.all:
            if str(item) in str(i):
                return int(i.split(" - ")[0])
        raise NameError(f"Could not locate {item}")

    def _build_headers(self, **extra_items) -> dict[str, str]:
        """_build_headers

        Creates the headers dictionary for a request

        Returns:
            dict[str, str]: request headers
        """
        headers: dict[str, str] = {
            "Content-Type": self.content_type,
            "Authorization": self.token,
        }  #: required headers for all calls
        if extra_items:  #: load additional itmes if any
            for k, v in extra_items.items():
                headers[k] = v
        return headers

    def _get_raw_data(
        self, headers: dict[str, str], params: dict[str, str] = None
    ):
        """_get_raw_data

        Given an API call, retrieve the raw response data.

        Args:
            headers (dict[str, str]): headers for the API request
            params (dict[str, str], optional): Optional query parameters.
            Defaults to None.

        """
        if params:  #: if params exist, add them to the request
            query: str = self._build_params(params)
            return request(
                "GET",
                url=self.page_url,
                headers=self._build_headers(headers),
                data=query,
            )
        return request(
            "GET", url=self.page_url, headers=self._build_headers(headers)
        )

    def get_all(self, **extra_headers):
        """get_all

        Get all requested items from the resource

        Returns:
            dict: returned data from the call
        """
        return self._decode_response(self._get_raw_data(**extra_headers))

    @property
    def all(self):
        """all

        Get a list of all the Resource objects
        """
        return self._list_all()

    def get(self, pk: int | str) -> dict[str, str]:
        """get

        Return data for a specific item available at the resource.

        Args:
            pk (int | str): an id or referential text for the search

        Returns:
            dict[str, str]: data for the found item.
        """
        if type(pk) is str:  #: get the actual id if not provided.
            pk = self._find(pk)
        return self._decode_response(
            request(
                "GET",
                url=f"{self.page_url}/{pk}",
                headers=self._build_headers(),
            )
        )


class Client(HaloResource):
    def __init__(
        self,
        token: str,
        page: str = "Client",
        list_value: str = "clients",
        content_type: str = CONTENT_TYPE,
        params: dict[str, str] = dict(),
    ) -> None:
        super().__init__(token, page, list_value, content_type, params)


class Agent(HaloResource):
    def __init__(
        self,
        token: str,
        page: str = "Agent",
        list_value: str = "agents",
        content_type: str = CONTENT_TYPE,
        params: dict[str, str] = dict(),
    ) -> None:
        super().__init__(token, page, list_value, content_type, params)


class Ticket(HaloResource):
    def __init__(
        self,
        token: str,
        page: str = "Tickets",
        list_value: str = "tickets",
        content_type: str = CONTENT_TYPE,
        params: dict[str, str] = dict(),
    ) -> None:
        super().__init__(token, page, list_value, content_type, params)

    def _list_all(self, title: str = "idsummary"):
        return super()._list_all(title)
