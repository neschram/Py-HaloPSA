from requests import get as GET, Response


class BaseData:
    """
    BaseData
    ========

        A class to manage API data such as headers, parameters,
        and response data.

    Example:
    --------

        >>> from halo_psa.utils import BaseData
        >>> test_data = BaseData(hello="world", foo="bar")
        >>> test_data()
        {'hello': 'world', 'foo': 'bar'}
        >>> test_data.list_options()
        ['hello', 'foo']
        >>> test_data.get("foo")
        'bar'
        >>> test_data.add("new_value", 1)
        >>> test_data()
        {'hello': 'world', 'foo': 'bar', 'new_value', 1}
        >>> test_data.remove("new_value")
        >>> test_data()
        {'hello': 'world', 'foo': 'bar'}

    """

    __FIELDS__: list[str] = ...

    def __init__(self, fields: dict[str, any] = dict(), **kwargs) -> None:
        """__init__

        Add data as an instance attribute if provided.

        Gives the option to provide data in a few ways:

        - provide data in a `fields` dictionary
        - add data through key, value kwargs to the call
        - a combination of both

        Example:
            >>> from halo_psa.core import BaseData
            >>> # From a dictionary
            >>> data_dict = {'name': 'test data'}
            >>> test_data = BaseData(data_dict)
            >>> test_data()
            {'name': 'test data'}
            >>> # From kwds only
            >>> test_data = BaseData(name='test data from kwds')
            >>> test_data()
            {'name': 'test data from kwds'}
            >>> # A mixture of both
            >>> test_data = BaseData(data_dict, is_example=True)
            >>> test_data()
            {'name': 'test data from kwds', 'is_example': True}

        """

        fields: dict[str, any] = fields
        fields.update(kwargs)
        self.__FIELDS__: list[str] = []
        for k, v in fields.items():
            self.__FIELDS__.append(k)
            self.add(k, v)

    def _field_exists(self, name: str) -> bool:
        return name in self.fields

    def _attr_exists(self, name: str) -> bool:
        return name in dir(self)

    def _exists(self, name: str) -> bool:
        if self._field_exists(name) and self._attr_exists(name):
            return True
        return False

    @property
    def fields(self):
        return self.__FIELDS__

    def __call__(self, **extra: dict[str, any]) -> dict[str, any]:
        """__call__

        Retrieve the instance's data. If additonal kwargs are provided,
        return those values updated with the instance's data instead.
        """
        data = {field: self.get(field) for field in self.fields}
        data.update(extra)
        return data

    def add(self, name: str, value: any) -> None:
        """add

        Add new data to the instance.

        Args:
            name (str): The data's name
            value (str): The data's value
        """
        self.__FIELDS__.append(name)
        setattr(self, name, value)

    def remove(self, name: str) -> None:
        """remove

        Remove data from the instance

        Args:
            name (str): the key to remove
        """
        if self._field_exists(name):
            self.__FIELDS__.remove(name)
        if self._attr_exists(name):
            delattr(self, name)

    def get(self, name: str) -> int | float | str | bool:
        """get

        Get data values from the instance.

        Args:
            name (str): The data's name

        Returns:
            str: The data's value
        """
        return getattr(self, name)


class BaseResource(BaseData):
    RESOURCE_PAGE: str = ...
    """Page  name for the resource"""
    RESOURCE_DATA: str = ...
    """name of the response container with resource items"""
    LIST_PARAMS: dict[str, any] = ...
    """query parameters for a get request to the resource"""

    def __init__(
        self,
        page: str = RESOURCE_PAGE,
        data_group: str = RESOURCE_DATA,
        fields: dict[str, any] = dict(),
        **kwargs,
    ) -> None:
        self.page: str = page
        self.data_group: str = data_group
        super().__init__(fields, **kwargs)

    def _GET(
        self,
        auth: dict[str, str],
        headers: dict[str, str],
        params: dict[str, str],
        pk: int = None,
    ) -> Response:
        # set the GET request URL
        _url: str = self.page
        if pk:
            _url += f"/{pk}"
        # build request headers
        _headers: dict[str, str] = auth
        if headers:
            _headers.update(headers)
        # get the response data
        response: Response = GET(url=_url, headers=_headers, params=params)
        return response

    def all(
        self,
        auth: dict[str, str],
        headers: dict[str, str],
        params: dict[str, str],
    ) -> dict[str, any]:
        response = self._GET(auth=auth, headers=headers, params=params)
        return response.json()
