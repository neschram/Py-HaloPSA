# halo_api/resources/clients.py

from halo_api.resources.base import BaseResource, ResourceInstance as Instance
from halo_api.core.utils import default_parameters, default_headers

_DEFAULT_PARAMS = default_parameters


class ClientInstance(Instance):
    """ClientInstance

    Attributes:

        INSTANCE_NAME (str): "Client"
        INSTANCE_FIELD_NAMES (list[str]): ["id", "name", "colour"]

    """

    INSTANCE_NAME: str = "Client"
    INSTANCE_FIELD_NAMES: list[str] = ["id", "name", "colour"]


class ClientResource(BaseResource):
    """class ClientResource

    Endpoint for HaloPSA Client (Customer) records.
    https://haloacademy.halopsa.com/apidoc/resources/clients

    """

    # Clients get parameters
    PAGINATE: bool = False
    """Do not paginate the response"""
    COUNT: int = 1500
    """Include up to 1500 instances in the reponse"""
    ORDER: str = "id"
    """Order by id"""
    INCLUDE_INACTIVE: bool = True
    """Include inactive instances"""
    INCLUDE_ACTIVE: bool = True
    """Include active instances"""
    ORDER_DESC: bool = False
    """Order Ascending (or do not order descending)"""
    PAGE_SIZE: int = None
    """We are not using pagination, there is no need for a page size"""
    PAGE_NO: int = None
    """We are not using pagination, there is only 1 page"""
    SEARCH: str = None
    """Do not inlcude a search string by default"""
    TOP_LEVEL_ID: int = None
    """Do not filter by a Top Level"""

    INSTANCE_CLASS: Instance = ClientInstance
    """The Instance class for :class:`ClientResource`"""
    RESOURCE_NAME: str = "Client"
    """Client is the HaloPSA Resource for Clients"""
    RESOURCE_LIST_PAGE: str = RESOURCE_NAME
    """The page name for the Resource's API Endpoint"""
    """Default request headers for the Resource's API calls"""
    RESOURCE_DATA_GROUP: str = "clients"
    """Response content is stored in the 'clients' content list"""
    RESOURCE_PARAMS: dict[str, str] = _DEFAULT_PARAMS(
        paginate=PAGINATE,
        count=COUNT,
        order=ORDER,
        includeinactive=INCLUDE_INACTIVE,
        includeactive=INCLUDE_ACTIVE,
        orderdesc=ORDER_DESC,
        page_size=PAGE_SIZE,
        page_no=PAGE_NO,
        search=SEARCH,
        toplevel_id=TOP_LEVEL_ID,
    )  #: Combines class attributes into a params dictionary for requests

    def __init__(
        self,
        RESOURCE_NAME=RESOURCE_NAME,
        RESOURCE_DATA_GROUP=RESOURCE_DATA_GROUP,
        RESOURCE_LIST_PAGE=RESOURCE_LIST_PAGE,
        RESOURCE_PARAMS=RESOURCE_PARAMS,
        RESOURCE_HEADERS=default_headers(),
        INSTANCE_CLASS=INSTANCE_CLASS,
        INSTANCES=ClientInstance,
        **kwargs,
    ):
        super().__init__(
            RESOURCE_NAME,
            RESOURCE_DATA_GROUP,
            RESOURCE_LIST_PAGE,
            RESOURCE_PARAMS,
            RESOURCE_HEADERS,
            INSTANCE_CLASS,
            INSTANCES,
            **kwargs,
        )
