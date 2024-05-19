from halo_api.settings import RESOURCE_SERVER
from halo_api.utils import (
    default_headers,
    default_parameters,
    Get,
)

_DEFAULT_HEADERS: dict[str, str] = default_headers()
_DEFAULT_PARAMETERS: dict[str, str] = default_parameters()


class ResourceInstance:
    """ResourceInstance

    An object returned by  `Resource.get_all()`

    Attributes:
        INSTANCE_NAME (str): The name of the instance.
        INSTANCE_FIELD_NAMES (list[str]): Data field names for the instance.

    """

    INSTANCE_NAME: str = "Instance"
    INSTANCE_FIELD_NAMES: list[str] = []

    def __init__(
        self,
        pk: int,
        name: str,
        fields: list[str] = INSTANCE_FIELD_NAMES,
        headers: dict[str, str] = _DEFAULT_HEADERS,
        **kwargs,
    ) -> None:
        """__init__

        Resource Instance

        Args:
            pk (int): numerical identificaiton of the instance
            name (str): textual identification of the instance
            fields (list[str], optional): instance field names.
            Defaults to INSTANCE_FIELD_NAMES.
            headers (dict[str, str], optional): instance request headers.
            Defaults to _DEFAULT_HEADERS.
        """
        self._pk: int = pk
        self._name: str = name
        self._headers: dict[str, str] = headers
        self.__fields__: list[str] = fields
        if kwargs:  #: if intial field data is provided
            for k, v in kwargs.items():
                setattr(self, k, v)  #: set the attribute
        self._params: dict[str, str] = _DEFAULT_PARAMETERS.update(
            {field: self.get(field) for field in self.fields}
        )

    @property
    def post_params(self) -> dict[str, str]:
        return self._post_params

    @post_params.setter
    def post_params(self, params: dict[str, str]):
        self._post_params.update(params)

    @post_params.deleter
    def post_params(self) -> None:
        self._post_params = self.INSTANCE_POST_PARAMS

    @property
    def fields(self) -> list[str]:
        return self.__fields__

    @fields.setter
    def fields(self, field) -> None:
        self.__fields__.append(field)

    def get(self, field_name: str) -> any:
        """get

        Returns the attribute value, `field_name` from the instance.
        """
        return getattr(self, field_name) or None

    def __str__(self) -> str:
        """__str__

        The instance's title: "Instance Name #_pk: _name"
        """
        return f"{self.INSTANCE_NAME} #{self._pk}: {self._name}"


class Resource:
    """Resource

    An API endpoint or "Resource" as defined by the HaloPSA API:
    https://haloservicedesk.com/apidoc/resources

    Attributes:
        RESOURCE_NAME (str): The name of the API Resource
        RESOURCE_DATA_GROUP (str): The group containing resource data in
        response content.
        RESOURCE_LIST_PAGE (str): The API endpoint name
        RESOURCE_GET_PARAMS (dict[str, str]): Default get request parameters
        RESOURCE_POST_PARAMS (dict[str, str]): Default post request parameters
        RESOURCE_HEADERS (dict[str, str]): Default request headers
        INSTANCE_CLASS (object): The class name for Resource instances

    METHODS:
        get_all(self) -> dict[int, "Resource"]: return all instances
        get(self, pk: int) -> dict[int, "Resource"]: return a single instance
    """

    RESOURCE_NAME: str = "Resource"
    RESOURCE_DATA_GROUP: str = RESOURCE_NAME.lower()
    RESOURCE_LIST_PAGE: str = RESOURCE_NAME
    RESOURCE_PARAMS: dict[str, str] = _DEFAULT_PARAMETERS
    RESOURCE_HEADERS: dict[str, str] = _DEFAULT_HEADERS
    INSTANCE_CLASS: "ResourceInstance" = ResourceInstance

    def __init__(
        self,
        name: str = RESOURCE_NAME,
        data_group: str = RESOURCE_DATA_GROUP,
        resource_page: str = RESOURCE_LIST_PAGE,
        params: dict[str, str] = RESOURCE_PARAMS,
        headers: dict[str, str] = RESOURCE_HEADERS,
        object_type: "ResourceInstance" = INSTANCE_CLASS,
    ):
        self._name: str = name
        self._data_group: str = data_group
        self._resource_page: str = resource_page
        self._params: dict[str, str] = params
        self._headers: dict[str, str] = headers
        self._object_type: "ResourceInstance" = object_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def data_group(self) -> str:
        return self._data_group

    @property
    def list_url(self) -> str:
        f"{RESOURCE_SERVER}/{self._resource_page}"

    @property
    def params(self) -> dict[str, str]:
        return self._params

    @params.setter
    def params(self, data: dict[str, str]) -> None:
        self._params.update(data)

    @property
    def headers(self) -> dict[str, str]:
        return self._headers

    @headers.setter
    def headers(self, data: dict[str, str]) -> None:
        self._headers.update(data)

    _GET: Get = Get(
        page=list_url,
        list_value=data_group,
        params=params,
        headers=headers,
    )

    def get_all(self) -> dict[int, "Resource"]:
        """_get_all

        Get all Resource instances.
        """
        return self._GET.get()

    def get(self, pk: int) -> dict[int, "Resource"]:
        """_get

        Get a single Resource instance.
        """
        return self._GET.get(items=pk)
