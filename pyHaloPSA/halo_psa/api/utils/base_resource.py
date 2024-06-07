import requests
from halo_psa.config import settings

RESOURCE_URL: str = settings.RESOURCE_SERVER


class BaseResource:
    """
    BaseResource
    ============

        BaseResource is the basic structure of a HaloPSA
        resource object. The information available from HaloPSA can be
        accessed at https://haloacademy.halopsa.com/apidoc/resources.

    Class Attributes:
    -----------------

        When subclassing `BaseResource` be sure to include
        the following class attributes:

        `RESOURCE_PAGE` (str): The Resource's page name
        `RESOURCE_DATA` (str): Response dictionary key that contains resource
        record data.
        `LIST_PARAMS` (dict[str, any]): Query parameters for a GET request.

    Example:
    --------

        >>> class SuppliersResource(BaseResource):
        >>>     RESOURCE_PAGE: str = "Supplier"
        >>>     RESOURCE_DATA: str = "suppliers"
        >>>     PAGENATE: bool = False
        >>>     PAGE_SIZE: int = 0
        >>>     PAGE_NO: int = 0
        >>>     ORDER: str = "ID"
        >>>     ORDER_DESC: bool = False
        >>>     SEARCH: str = None
        >>>     COUNT: int = 5000
        >>>     TOPLEVEL_ID: int = None
        >>>     INCLUDE_INACTIVE: bool = True
        >>>     INCLUDE_ACTIVE: bool = True
        >>>     LIST_PARAMS: dict[str, str] = {
        >>>        "pageinate": PAGENATE,
        >>>        "page_size": PAGE_SIZE,
        >>>        "page_no": PAGE_NO,
        >>>        "order": ORDER,
        >>>        "orderdesc": ORDER_DESC,
        >>>        "search": SEARCH,
        >>>        "count": COUNT,
        >>>        "toplevel_id": TOPLEVEL_ID,
        >>>        "includeinactive": INCLUDE_INACTIVE,
        >>>        "includeactive": INCLUDE_ACTIVE,
        >>>    }
        >>>    def __init__(
        >>>        self,
        >>>        list_url: str = f"{RESOURCE_SERVER}/{RESOURCE_PAGE}",
        >>>        data_group: str = RESOURCE_DATA,
        >>>        **extra,
        >>>    ) -> None:
        >>>        super().__init__(list_url, data_group, **extra)

    """

    RESOURCE_PAGE: str = ...
    """Page  name for the resource"""
    RESOURCE_DATA: str = ...
    """name of the response container with resource items"""
    LIST_PARAMS: dict[str, any] = ...
    """query parameters for a get request to the resource"""

    def __init__(
        self,
        page: str = RESOURCE_PAGE,
        data_group: str = RESOURCE_DATA,
        **extra,
    ):
        self._page: str = page
        self._data_group: str = data_group
        super().__init__(**extra)

    def _request_resource(
        self, headers: dict[str, str], query: dict[str, any]
    ) -> list | dict:
        """_request_resource

        Execute an API request to the resource.

        Args:
            headers (dict[str, str]): Request headers
            query (dict[str, any]): Request query parameters

        Returns:
            list | dict: Response data
        """
        return requests.get(
            url=self.list_url,
            headers=headers,
            params=query,
        ).json()

    def get_resource_count(self) -> int:
        """get_resource_count

        Get the number of records available at the resource.

        Returns:
            int: count of resource items (records)
        """
        return self._request_resource()["record_count"]

    def get_resource_items(self) -> dict[str, any]:
        """get_resource_items

        Returns resource records from an API call to the resource.

        Returns:
            dict: Resource records from the request's response data.
        """
        return self._request_resource()[self.data_group]

    @property
    def page(self):
        """page

        Same as RESOURCE_PAGE but with less typing.

        Returns:
            str: Url to the resource.
        """
        return self._page

    @property
    def list_url(self) -> str:
        """The full API endpoint url for the resource"""
        return f"{self.page}"

    @property
    def data_group(self) -> str:
        """Response container with list data."""
        return self._data_group

    def get(
        self,
        auth: dict[str, str],
        headers: dict[str, str] = None,
        params: dict[str, str] = None,
        pk: int = None,
    ):
        _url: str = self.page
        # set the auth headers first
        _headers: dict[str, str] = auth
        if headers:
            # update the headers with additional values
            _headers.update(headers)
        # one or all records?
        if pk is not None:
            # add the record id to the request URL
            _url += f"/{pk}"

        if self.data_group is not None:
            return requests.get(
                url=_url, headers=_headers, params=params
            ).json()[self.data_group]
        return requests.get(url=_url, headers=_headers, params=params).json()
