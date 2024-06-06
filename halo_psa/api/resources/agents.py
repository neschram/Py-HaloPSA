from halo_psa.config.settings import RESOURCE_SERVER
from .base_resource import BaseResource


class Agents(BaseResource):
    """Agents

    Endpoint for Agent accounts and their preferences and permissions.

    List Parameters:
        TEAM (str): Filter by Agents within a particular team
        SEARCH (str): Filter by Agents with a name, email address or telephone
        number
        SECTION_ID (int): Filter by Agents within a particular team
        DEPARTMENT_ID (int): Filter by Agents within a particular department
        CLIENT_ID (int): Filter by Agents who have access to a particular
        client
        ROLE (str): Filter by Agents who have a particular role.
        Requires an int passed as a string.
        INCLUDE_ENABLED (bool): Include enabled Agents in the response
        INCLUDE_DISABLED (bool): Include disabled Agents in the response
        INCLUDE_UNASSIGNED (bool): Include the unassigned Agent in the response
        INCLUDE_DISABLED (bool): Include disabled Agents in the response

    Lookup Parameters:
        INCLUDE_DETAILS (bool): Whether to include extra objects
        Defaults to True.
        INCLUDE_ACTIVITY (bool): Whether to include customer ticket activity
        Defaults to False.
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
    """Filter by Agents who have a particular role ID."""
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
