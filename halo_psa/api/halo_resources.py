from halo_psa.config.settings import RESOURCE_SERVER
from .base_resource import BaseResource


class Clients(BaseResource):
    """
    Clients
    =======

    Returns an object containing the count of Clients, and an array of Client
    objects.
    https://haloacademy.halopsa.com/apidoc/resources/clients

    Attributes:

        RESOURCE_PAGE (str): Client
        RESOURCE_DATA (str): clients

    List Params:

        pageinate (bool): False
        page_size (int): 0
        page_no (int): 0
        order (str): ID
        orderdesc (bool): False
        search (str): None
        toplevel_id (int): None
        includeinactive (bool): True
        includeactive (bool): True
        count (int): 5000

    Lookup Params:

        includedetails (bool): True
        includeactivity (bool): False

    """

    # Resource Attributes
    RESOURCE_PAGE: str = "Client"
    RESOURCE_DATA: str = "clients"

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
    """Include active Customers in the response"""
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
        data_group: str = RESOURCE_DATA,
        **extra,
    ):
        super().__init__(list_url, data_group, **extra)


class Agents(BaseResource):
    """
    Agents
    ======

    Returns an object containing the count of Agents, and an array of Agent
    objects.
    https://haloacademy.halopsa.com/apidoc/resources/agents

    Attributes:

        RESOURCE_PAGE (str): Agent
        RESOURCE_DATA (str): None

    List Params:

        team (str): None
        search (str): None
        section_id (int): None
        department_id (int): None
        client_id (int): None
        role (str): None
        includeenabled (bool): True
        includedisabled (bool): True
        includeunassigned (bool): True
        includedisabled (bool): True

    Lookup Params:

        includedetails (bool): True
        include_activity (bool): False
    """

    # Resource Attributes
    RESOURCE_PAGE: str = "Agent"
    RESOURCE_DATA: str = None

    # Default List Params
    TEAM: str = None
    """Filter by Agents within a particular team"""
    SEARCH: str = None
    """Filter by Agents with a name, email address or telephone number"""
    SECTION_ID: int = None
    """Filter by Agents within a particular team"""
    DEPARTMENT_ID: int = None
    """Filter by Agents within a particular department"""
    CLIENT_ID: int = None
    """Filter by Agents who have access to a particular client"""
    ROLE: str = None
    """Filter by Agents who have a particular role."""
    INCLUDE_ENABLED: bool = True
    """Include enabled Agents in the response"""
    INCLUDE_DISABLED: bool = True
    """Include disabled Agents in the response"""
    INCLUDE_UNASSIGNED: bool = True
    """Include the unassigned Agent in the response"""
    INCLUDE_DISABLED: bool = True
    """Include disabled Agents in the response"""

    # Default Lookup Params (RESOURCE_PAGE/ID)
    INCLUDE_DETAILS: bool = True
    """Whether to include extra objects in the response"""

    LIST_PARAMS: dict[str, str] = {
        "team": TEAM,
        "search": SEARCH,
        "section_id": SECTION_ID,
        "department_id": DEPARTMENT_ID,
        "client_id": CLIENT_ID,
        "role": ROLE,
        "includeenabled": INCLUDE_ENABLED,
        "includedisabled": INCLUDE_DISABLED,
        "includeunassigned": INCLUDE_UNASSIGNED,
        "includedisabled": INCLUDE_DISABLED,
    }

    def __init__(
        self,
        list_url: str = f"{RESOURCE_SERVER}/{RESOURCE_PAGE}",
        data_group: str = RESOURCE_DATA,
        **extra,
    ):
        super().__init__(list_url, data_group, **extra)


class Assets(BaseResource):
    """
    Assets
    =======

    Returns an object containing the count of Assets, and an array of Asset
    objects.
    https://haloacademy.halopsa.com/apidoc/resources/assets

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
    ASSETGROUP_ID: int = None
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


class Suppliers(BaseResource):
    """
    Suppliers
    =======

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
