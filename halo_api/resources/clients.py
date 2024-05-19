# Py-HaloPSA
from halo_api.resources.base import BaseResource, ResourceInstance as Instance
from halo_api.core.utils import default_parameters

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

    Prarmeters:
    -----------

        INSTANCE_CLASS (Instance):
            :class:`ClientInstance`
        RESOURCE_NAME (str):
            Client
        RESOURCE_DATA_GROUP (str):
            clients
        RESOURCE_PARAMS (dict[str, any]):
            Get parameters as noted in :ref:`Client Query (GET) Parameters`

    Client Query (GET) Parameters:
    ------------------------------

        PAGINATE (bool):
            Whether to use Pagination in the response. Defaults to False.
        COUNT (int):
            When not using pagination, the number of results to return.
            Defaults to 1500.
        ORDER (str):
            The name of the field to order by. Defaults to "id".
        INCLUDE_INACTIVE (bool):
            Include inactive Customers in the response. Defaults to True.
        INCLUDE_ACTIVE (bool):
            Include active Customers in the response. Defaults to True.
        ORDER_DESC (bool):
            Whether to order ascending or descending. Defaults to False.
        PAGE_SIZE (int):
            When using Pagination, the size of the page. Defaults to None.
        PAGE_NO (int):
            When using Pagination, the page number to return. Defaults to None.
        SEARCH (str):
            Filter by Customers like your search string. Defaults to None.
        TOP_LEVEL_ID (int): None


    """

    # Clients get parameters
    PAGINATE: bool = False
    COUNT: int = 1500
    ORDER: str = "id"
    INCLUDE_INACTIVE: bool = True
    INCLUDE_ACTIVE: bool = True
    ORDER_DESC: bool = False
    PAGE_SIZE: int = None
    PAGE_NO: int = None
    SEARCH: str = None
    TOP_LEVEL_ID: int = None

    INSTANCE_CLASS: Instance = ClientInstance
    RESOURCE_NAME: str = "Client"
    RESOURCE_DATA_GROUP: str = "clients"
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
    )