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

    An object returned by  ``Resource.get_all()``
    """

    INSTANCE_ID_FIELD: str = "id"
    """Field name of the instance's identifying integer."""
    INSTANCE_TITLE_FIELD: str = "name"
    """Field name of the instance's identifying text."""
    INSTANCE_FIELD_NAMES: list[str] = []
    """Data field names for the instance."""
    INSTANCE_HEADERS: dict[str, str] = _DEFAULT_HEADERS()
    """Instance request headers."""
    INSTANCE_GET_PARAMS: dict[str, str] = _DEFAULT_PARAMETERS()
    """Query parameters for the instance's GET request."""

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

    Each HaloPSA API Resource should subclass this `BaseResource` class.
    It includes standard requirements for handling API requests throughout
    the HaloPSA API endpoint.

    """

    RESOURCE_NAME: str = "Resource"
    """The HaloPSA API Resource's name"""
    RESOURCE_DATA_GROUP: str = RESOURCE_NAME.lower()
    """The response container that house's desired content data"""
    RESOURCE_LIST_PAGE: str = RESOURCE_NAME
    """The page name for the Resource's API Endpoint"""
    RESOURCE_PARAMS: dict[str, str] = _DEFAULT_PARAMETERS()
    """Default GET Parameters for the ``Resource``"""
    RESOURCE_HEADERS: dict[str, str] = _DEFAULT_HEADERS()
    """Default request headers for the Resource's API calls"""
    INSTANCE_CLASS: "ResourceInstance" = ResourceInstance
    """The class object that all ``Resource`` items should instanciate"""
    INSTANCES: dict[int, "ResourceInstance"] = {}
    """A dictionary of created ``ResourceInstance`` objects"""

    def __init__(self, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                self.__setattr__(k, v)

    @property
    def name(self) -> str:
        """name

        The Resource's identifying name

        Returns:
            str: `self.RESOURCE_NAME
        """
        return self.RESOURCE_NAME

    @property
    def data_group(self) -> str:
        """data_group

        The response container that house's desired content data
        """
        return self.RESOURCE_DATA_GROUP

    @property
    def list_url(self) -> str:
        """list_url

        The full web url of the Resource's API page

        Returns:
            str: f"{RESOURCE_SERVER}/{self.RESOURCE_LIST_PAGE}"
        """
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
        """_build_instance

        Create a ``ResourceInstance`` object

        Args:
            instance_data (dict): ResourceInstance attributes
            add (bool, optional): Add to the Resource's INSTANCES.
                Defaults to False.

        Returns:
            ResourceInstance: A ResourceInstance object with the supplied attributes.
        """
        if add:
            instance = self.INSTANCE_CLASS(**instance_data)
            self._add_instance(instance)
        return self.INSTANCE_CLASS(**instance_data)

    def _add_instance(self, instance: "ResourceInstance") -> None:
        """_add_instance

        Add a ResourceInstance to the Resource's INSTANCES dictionary

        Args:
            instance (ResourceInstance): The instance to add
        """
        self.INSTANCES.update({instance._pk: instance})
