from halo_psa.config.settings import RESOURCE_SERVER
from halo_psa.core import BaseResource


class AssetsResource(BaseResource):
    """
    AssetsResource
    ==============

    Returns an object containing the count of Assets, and an array of Asset
    objects.
    https://haloacademy.halopsa.com/apidoc/resources/assets

    .. Note::

        The only way I have been successful at retrieving assets is by ensuring
        my custom API integration has "all" checked in the Permissions tab.

    Attributes:

        RESOURCE_PAGE (str): Asset
        RESOURCE_DATA (str): assets

    List Params:

        pageinate (bool): False
        page_size (int): 0
        page_no (int): 0
        order (string): id
        orderdesc (bool): True
        search (string): None
        count (int): 5000
        ticket_id (int): None
        client_id (int): None
        site_id (int): None
        username (string): None
        assetgroup_id (int): None
        assettype_id (int): None
        linkedto_id (int): None
        includeinactive (bool): True
        includeactive (bool): True
        includechildren (bool): True
        contract_id (int): None

    Lookup Params:

        includedetails (bool): True
        includediagramdetails (bool): True

    """

    # Resource Attributes
    RESOURCE_PAGE: str = "Asset"
    RESOURCE_DATA: str = "assets"

    # Default List Params
    PAGENATE: bool = False
    """Whether to use Pagination in the response"""
    PAGE_SIZE: int = 0
    """When using Pagination, the size of the page"""
    PAGE_NO: int = 0
    """When using Pagination, the page number to return"""
    ORDER: str = "id"
    """The name of the field to order by"""
    ORDER_DESC: bool = True
    """Whether to order ascending or descending"""
    SEARCH: str = None
    """Filter by Assets like your search string"""
    COUNT: int = 5000
    """When not using pagination, the number of results to return"""
    TICKET_ID: int = None
    """Filter by Assets belonging to a particular ticket"""
    CLIENT_ID: int = None
    """Filter by Assets belonging to a particular client"""
    SITE_ID: int = None
    """Filter by Assets belonging to a particular site"""
    USERNAME: str = None
    """Filter by Assets belonging to a particular user"""
    ASSETGROUP_ID: int = 106
    """Filter by Assets belonging to a particular Asset group"""
    ASSETTYPE_ID: int = None
    """Filter by Assets belonging to a particular Asset type"""
    LINKEDTO_ID: int = None
    """Filter by Assets linked to a particular Asset"""
    INCLUDE_INACTIVE: bool = True
    """Include inactive Assets in the response"""
    INCLUDE_ACTIVE: bool = True
    """Include active Assets in the response"""
    INCLUDE_CHILDREN: bool = True
    """Include child Assets in the response"""
    CONTRACT_ID: int = None
    """Filter by Assets assigned to a particular contract"""

    LIST_PARAMS: dict[str, any] = {
        "pageinate": PAGENATE,
        "page_size": PAGE_SIZE,
        "page_no": PAGE_NO,
        "order": ORDER,
        "orderdesc": ORDER_DESC,
        "search": SEARCH,
        "count": COUNT,
        "ticket_id": TICKET_ID,
        "client_id": CLIENT_ID,
        "site_id": SITE_ID,
        "username": USERNAME,
        "assetgroup_id": ASSETGROUP_ID,
        "assettype_id": ASSETTYPE_ID,
        "linkedto_id": LINKEDTO_ID,
        "includeinactive": INCLUDE_INACTIVE,
        "includeactive": INCLUDE_ACTIVE,
        "includechildren": INCLUDE_CHILDREN,
        "contract_id": CONTRACT_ID,
    }

    # Default Lookup Params (RESOURCE_PAGE/ID)
    INCLUDE_DETAILS: bool = True
    """Whether to include extra objects in the response"""
    INCLUDE_DIAGRAM_DETAILS: bool = True
    """Whether to include diagram details in the response"""

    def __init__(
        self,
        list_url: str = f"{RESOURCE_SERVER}/{RESOURCE_PAGE}",
        data_group: str = RESOURCE_DATA,
        **extra,
    ):
        super().__init__(list_url, data_group, **extra)
