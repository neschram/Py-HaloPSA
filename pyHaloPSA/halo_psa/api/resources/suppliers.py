from halo_psa.config.settings import RESOURCE_SERVER
from .base_resource import BaseResource


class SuppliersResource(BaseResource):
    """
    SuppliersResource
    =================

    Returns an object containing the count of Suppliers,
    and an array of Supplier objects.

    https://haloacademy.halopsa.com/apidoc/resources/suppliers

    Attributes:

        RESOURCE_PAGE (str): Supplier
        RESOURCE_DATA (str): suppliers

    List Params:

        pageinate (bool): False
        page_size (int): 0
        page_no (int): 0
        order (str): ID
        orderdesc (bool): False
        search (str): None
        count (int): 5000
        toplevel_id (int): None
        includeinactive (bool): True
        includeactive (bool): True

    Lookup Params:

        includedetails (bool): True

    """

    # Resource Attributes
    RESOURCE_PAGE: str = "Supplier"
    RESOURCE_DATA: str = "suppliers"

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
    COUNT: int = 5000
    """When not using pagination, the number of results to return"""
    TOPLEVEL_ID: int = None
    """Filter by Customers belonging to a particular top level"""
    INCLUDE_INACTIVE: bool = True
    """Include inactive Customers in the response"""
    INCLUDE_ACTIVE: bool = True
    """Include active Customers in the response"""

    # Default Lookup Params (RESOURCE_PAGE/ID)
    INCLUDE_DETAILS: bool = True
    """Whether to include extra objects in the response"""

    LIST_PARAMS: dict[str, str] = {
        "pageinate": PAGENATE,
        "page_size": PAGE_SIZE,
        "page_no": PAGE_NO,
        "order": ORDER,
        "orderdesc": ORDER_DESC,
        "search": SEARCH,
        "count": COUNT,
        "toplevel_id": TOPLEVEL_ID,
        "includeinactive": INCLUDE_INACTIVE,
        "includeactive": INCLUDE_ACTIVE,
    }

    def __init__(
        self,
        list_url: str = f"{RESOURCE_SERVER}/{RESOURCE_PAGE}",
        data_group: str = RESOURCE_DATA,
        **extra,
    ):
        super().__init__(list_url, data_group, **extra)
