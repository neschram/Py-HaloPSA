from utils import BaseData
from config.settings import RESOURCE_SERVER
from .base_resource import BaseResource


class Clients(BaseResource):
    """
    Clients
    =======

    Returns an object containing the count of Clients, and an array of Client objects.
    https://haloacademy.halopsa.com/apidoc/resources/clients

    List Params:

        pageinate (bool): Whether to use Pagination in the response
        page_size (int): When using Pagination, the size of the page
        page_no (int): When using Pagination, the page number to return
        order (str): The name of the field to order by
        orderdesc (bool): Whether to order ascending or descending
        search (str): Filter by Customers like your search string
        toplevel_id (int): Filter by Customers belonging to a particular top level
        includeinactive (bool): Include inactive Customers in the response
        includeactive (bool): Include active Customers in the response
        count (int): When not using pagination, the number of results to return

    Lookup Params:

        id (int, required): The Customer's ID
        includedetails (bool): Whether to include extra objects in the response
        includeactivity (bool): Whether to include customer ticket activity in the response

    """

    # Resource Attributes
    RESOURCE_PAGE = "Client"
    RESOURCE_DATA = "clients"

    # Default List Params
    PAGENATE: bool = False
    """Whether to use Pagination in the response"""
    PAGE_SIZE: int = 0
    """When using Pagination, the size of the page"""
    PAGE_NO: int = 0
    """When using Pagination, the page number to return"""
    ORDER: str = "ID"
    """The name of the field to order by"""
    ORDER_DESC: bool = False
    """Whether to order ascending or descending"""
    SEARCH: str = None
    """Filter by Customers like your search string"""
    TOPLEVEL_ID: int = None
    """Filter by Customers belonging to a particular top level"""
    INCLUDE_INACTIVE: bool = True
    """Include inactive Customers in the response"""
    INCLUDE_ACTIVE: bool = True
    """Include inactive Customers in the response"""
    COUNT: int = 5000
    """When not using pagination, the number of results to return"""

    # Default Lookup Params (RESOURCE_PAGE/ID)
    INCLUDE_DETAILS: bool = True
    """Whether to include extra objects in the response"""
    INCLUDE_ACTIVITY: bool = False
    """Whether to include customer ticket activity in the response"""

    LIST_PARAMS: dict[str, str] = {
        "pageinate": PAGENATE,
        "page_size": PAGE_SIZE,
        "page_no": PAGE_NO,
        "order": ORDER,
        "orderdesc": ORDER_DESC,
        "search": SEARCH,
        "toplevel_id": TOPLEVEL_ID,
        "includeinactive": INCLUDE_INACTIVE,
        "includeactive": INCLUDE_ACTIVE,
        "count": COUNT,
    }

    def __init__(
        self,
        list_url: str = f"{RESOURCE_SERVER}/{RESOURCE_PAGE}",
        data_group: str = ...,
        **extra,
    ):
        super().__init__(list_url, data_group, **extra)
