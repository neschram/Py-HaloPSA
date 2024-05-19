# 3rd party
import requests

# Py-HaloPSA
from halo_api.config.settings import CONTENT_TYPE


def default_headers(**kwargs) -> dict[str, str]:
    """default_headers

    Standard headers required throughout the HaloPSA
    API.

    Returns:
        dict[str,str]: request header data
    """
    return {"Content-Type": CONTENT_TYPE}.update(kwargs)


def default_parameters(**kwargs) -> dict[str, str]:
    """default_parameters

    Standard parameters for the HaloPSA API endpoint.

    Returns:
        dict[str, str]: query parameter request data
    """
    return {}.update(kwargs)


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
