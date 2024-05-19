"""resources.base

Base Resouce objects used for each HaloPSA API Resource.
"""

# Py-HaloPSA
from halo_api.config.settings import RESOURCE_SERVER
from halo_api.core.utils import Get, default_headers, default_parameters

_DEFAULT_HEADERS: dict[str, str] = default_headers
_DEFAULT_PARAMETERS: dict[str, str] = default_parameters


class ResourceInstance:
    """ResourceInstance

    An object returned by  `Resource.get_all()`

    Attributes:

        INSTANCE_ID_FIELD (str): Field name of the instance's
        identifying integer. Defaults to `id`.
        INSTANCE_TITLE_FIELD (str): Field name of the instance's
        identifying text. Defaults to `"name"`.
        INSTANCE_FIELD_NAMES (list[str]): Data field names for the instance.
        Defaults to an empty list (`[]`).
        INSTANCE_HEADERS (dict[str, str]): Instance request headers.
        Defaults to `_DEFAULT_HEADERS()`.
        INSTANCE_GET_PARAMS (dict[str, str]): Query parameters for the
        instance's GET request. Defaults to `_DEFAULT_PARAMETERS()`.

    """

    INSTANCE_ID_FIELD: str = "id"
    INSTANCE_TITLE_FIELD: str = "name"
    INSTANCE_FIELD_NAMES: list[str] = []
    INSTANCE_HEADERS: dict[str, str] = _DEFAULT_HEADERS()
    INSTANCE_GET_PARAMS: dict[str, str] = _DEFAULT_PARAMETERS()

    def __init__(
        self,
        **kwargs,
    ) -> None:
        if kwargs:  #: if intial field data is provided
            for k, v in kwargs.items():
                if k not in self.fields:  #: add to self.fields
                    self.fields = k
                self.set(k, v)  #: set the attribute
        self._pk = self.get(self.INSTANCE_ID_FIELD)
        self._title = self.get(self.INSTANCE_TITLE_FIELD)

    @property
    def post_params(self) -> dict[str, str]:
        """post_params

        Available update fields for POST calls to the Resource instance.

        Returns:

            dict[str, str]: instance fields and their values.

        """
        return {field: self.get(field) for field in self.INSTANCE_FIELD_NAMES}

    @post_params.setter
    def post_params(self, params: dict[str, str]):
        """post_params.setter

        Update ResourceInstance post data with the provided
        field names and their values.

        Args:

            params (dict[str, str]): update fields

        """
        self._post_params.update(params)

    @post_params.deleter
    def post_params(self) -> None:
        self._post_params = {f: None for f in self.fields}

    @property
    def fields(self) -> list[str]:
        return self.INSTANCE_FIELD_NAMES

    @fields.setter
    def fields(self, field) -> None:
        self.INSTANCE_FIELD_NAMES.append(field)

    def get(self, field_name: str) -> any:
        """get

        Returns the attribute value, `field_name` from the instance.
        """
        return getattr(self, field_name) or None

    def set(self, field_name: str, value: any = None) -> None:
        if field_name not in self.fields:
            self.fields = field_name
        self.__setattr__(field_name, value)

    def __str__(self) -> str:
        """__str__

        The instance's title: "Instance Name #_pk: _title"
        """
        return f"{self.__class__.__name__} #{self._pk}: {self._title}"


class BaseResource:
    """Resource

    An API endpoint or "Resource" as defined by the HaloPSA API:
    https://haloservicedesk.com/apidoc/resources

    Attributes:

        RESOURCE_NAME (str): The name of the API Resource
        RESOURCE_DATA_GROUP (str): The group containing resource data in
            response content.
        RESOURCE_LIST_PAGE (str): The API endpoint name
        RESOURCE_GET_PARAMS (dict[str, str]): Default get request parameters
        RESOURCE_POST_PARAMS (dict[str, str]): Default post request
            parameters
        RESOURCE_HEADERS (dict[str, str]): Default request headers
        INSTANCE_CLASS (object): The class name for Resource instances

    METHODS:

        get_all(self) -> dict[int, "Resource"]: return all instances
        get(self, pk: int) -> dict[int, "Resource"]: return a single instance

    """

    RESOURCE_NAME: str = "Resource"
    RESOURCE_DATA_GROUP: str = RESOURCE_NAME.lower()
    RESOURCE_LIST_PAGE: str = RESOURCE_NAME
    RESOURCE_PARAMS: dict[str, str] = _DEFAULT_PARAMETERS()
    RESOURCE_HEADERS: dict[str, str] = _DEFAULT_HEADERS()
    INSTANCE_CLASS: "ResourceInstance" = ResourceInstance
    INSTANCES: dict[int, "ResourceInstance"] = {}

    def __init__(self, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                self.__setattr__(k, v)

    @property
    def name(self) -> str:
        return self.RESOURCE_NAME

    @property
    def data_group(self) -> str:
        return self.RESOURCE_DATA_GROUP

    @property
    def list_url(self) -> str:
        f"{RESOURCE_SERVER}/{self.RESOURCE_LIST_PAGE}"

    @property
    def params(self) -> dict[str, str]:
        return self.RESOURCE_PARAMS

    @params.setter
    def params(self, data: dict[str, str]) -> None:
        self.RESOURCE_PARAMS.update(data)

    @property
    def headers(self) -> dict[str, str]:
        return self.RESOURCE_HEADERS

    @headers.setter
    def headers(self, data: dict[str, str]) -> None:
        self.RESOURCE_HEADERS.update(data)

    _GET: Get = Get(
        page=list_url,
        list_value=data_group,
        params=params,
        headers=headers,
    )

    def _get_all(self) -> dict[int, "BaseResource"]:
        """_get_all

        Get all BaseResource instances.
        """
        data: dict = self._GET.get()
        for instance in data:
            self._build_instance(instance, add=True)
        return self.INSTANCES

    def _get(self, pk: int) -> dict[int, "BaseResource"]:
        """_get

        Get a single BaseResource instance.
        """
        instance = self._GET.get(items=pk)
        self.add_instance(instance)

    def get(self, pk: int, update: bool = False) -> dict[int, "BaseResource"]:
        """_get

        Get a single BaseResource instance.
        """
        if update:
            return self._get(pk=pk)
        try:
            return self._OBJECTS[pk]
        except KeyError:
            return self._get(pk=pk)

    def _build_instance(
        self, instance_data: dict, add: bool = False
    ) -> "ResourceInstance":
        if add:
            instance = self.INSTANCE_CLASS(**instance_data)
            self._add_instance(instance)
        return self.INSTANCE_CLASS(**instance_data)

    def _add_instance(self, instance: "ResourceInstance") -> None:
        self.INSTANCES.update({instance._pk: instance})
