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

    RESOURCE_PAGE (str): The Resource's page name
    RESOURCE_DATA (str): The response content container with data
    LIST_PARAMS (dict[str, any]): Resource Get params

    """

    RESOURCE_PAGE: str = ...
    """Page  name for the resource"""
    RESOURCE_DATA: str = ...
    """name of the response container with resource items"""
    LIST_PARAMS: dict[str, any] = ...
    """parameters for listing all resource items"""

    def __init__(
        self,
        page: str = RESOURCE_PAGE,
        data_group: str = RESOURCE_DATA,
        **extra,
    ):
        self._page: str = page
        self._data_group: str = data_group
        super().__init__(**extra)

    def _request_resource(self, headers, query):
        return requests.get(
            url=self.list_url,
            headers=headers,
            data=query,
        ).json()

    def get_resource_count(self):
        return self._request_resource()["record_count"]

    def get_resource_items(self):
        return self._request_resource()[self.data_group]

    @property
    def page(self):
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
        get_link: str = self.list_url
        heads: dict[str, str] = auth
        if headers:
            heads.update(headers)
        if pk is not None:
            get_link += f"/{pk}"
        if self.data_group is not None:
            return requests.get(
                url=get_link, headers=heads, params=params
            ).json()[self.data_group]
        return requests.get(url=get_link, headers=heads, params=params).json()
