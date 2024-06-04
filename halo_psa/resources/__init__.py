import requests
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
        data_group: str = RESOURCE_DATA,
        **extra,
    ):
        super().__init__(list_url, data_group, **extra)


class Agents(BaseResource):
    """
    team (str): Filter by Agents within a particular team
    search (str): Filter by Agents with a name, email address or telephone number like your search
    section_id (int): Filter by Agents within a particular team
    department_id (int): Filter by Agents within a particular department
    client_id (int): Filter by Agents who have access to a particular client
    role (str): Filter by Agents who have a particular role. Requires an int passed as a string
    includeenabled (bool): Include enabled Agents in the response
    includedisabled (bool): Include disabled Agents in the response
    includeunassigned (bool): Include the unassigned Agent in the response
    includedisabled (bool): Include disabled Agents in the response
    """

    # Resource Attributes
    RESOURCE_PAGE: str = "Agent"
    RESOURCE_DATA: str = None

    # Default List Params
    TEAM: str = None
    """Filter by Agents within a particular team"""
    SEARCH: str = None
    """Filter by Agents with a name, email address or telephone number like your search"""
    SECTION_ID: int = None
    """Filter by Agents within a particular team"""
    DEPARTMENT_ID: int = None
    """Filter by Agents within a particular department"""
    CLIENT_ID: int = None
    """Filter by Agents who have access to a particular client"""
    ROLE: str = None
    """Filter by Agents who have a particular role. Requires an int passed as a string"""
    INCLUDE_ENABLED: bool = None
    """Include enabled Agents in the response"""
    INCLUDE_DISABLED: bool = None
    """Include disabled Agents in the response"""
    INCLUDE_UNASSIGNED: bool = None
    """Include the unassigned Agent in the response"""
    INCLUDE_DISABLED: bool = None
    """Include disabled Agents in the response"""

    # Default Lookup Params (RESOURCE_PAGE/ID)
    INCLUDE_DETAILS: bool = True
    """Whether to include extra objects in the response"""
    INCLUDE_ACTIVITY: bool = False
    """Whether to include customer ticket activity in the response"""

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
