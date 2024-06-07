from halo_psa.config.settings import RESOURCE_SERVER
from halo_psa.core import BaseResource


class AgentsResource(BaseResource):
    """
    AgentsResource
    ==============

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
