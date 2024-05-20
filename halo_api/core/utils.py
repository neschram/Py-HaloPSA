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
    headers: dict[str, str] = {"Content-Type": CONTENT_TYPE}
    headers.update(kwargs)
    return headers


def default_parameters(**kwargs) -> dict[str, str]:
    """default_parameters

    Standard parameters for the HaloPSA API endpoint.

    Returns:
        dict[str, str]: query parameter request data
    """
    return {}.update(kwargs)


class Get:
    """Get

    Performs the task of sending an API GET Request
    to HaloPSA's API interface.
    """

    PAGE: str = None
    """API request page"""
    LIST_VALUE: str = None
    """name of the field storing data in the response"""
    PARAMS: dict[str, str] = None
    """query parameters to pass in the request"""
    HEADERS: dict[str, str] = None
    """http headers to pass in the request"""

    def __init__(
        self,
        page: str = PAGE,
        list_value: str = LIST_VALUE,
        params: dict[str, str] = PARAMS,
        headers: dict[str, str] = HEADERS,
    ) -> None:
        """__init__

        Initialize the Get object.

        Args:
            page (str): url of the API request page
            list_value (str): name of the content field in the response
            params (dict[str, any]): query parameters to pass in the request
            headers (dict[str, any]): http headers to pass in the request

        """
        self.page = page
        self.list_value = list_value
        self.params = params
        self.headers = headers

    def _all(self):
        """_all

        Query the Resource for data on all instances available

        Returns:
            dict [str, str]: a request response json dict filtered
            to the content container.
        """
        return requests.get(
            url=self.page, headers=self.headers, data=self.params
        ).json()[self.list_value]

    def _get_by_id(self, pk: int) -> dict[str, str]:
        """_get_by_id

        Query the Resource for data on a single instance by its id.

        Args:
            pk (int): the desired instance's id

        Returns:
            dict[str, str]: instance data
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
