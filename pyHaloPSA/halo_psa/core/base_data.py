class BaseData:
    """
    BaseData
    ========

    A class to manage request data such as headers
    and parameters for API calls.

    Example:
    --------

    Using HaloPSA's required content header::

        >>> from halo_psa.utils import BaseData
        >>> content_type = {
        >>>    "Content-Type":
        >>>    "application/x-www-form-urlencoded",
        >>> }
        >>> query_headers = BaseData(content_type)
        >>> query_headers()
        {'Content-Type': 'application/x-www-form-urlencoded'}
        >>> query_headers.list_options()
        ['Content-Type']
        >>> query_headers.get("Content-Type")
        'application/x-www-form-urlencoded'
        >>> query_headers.add("new value", 1)
        >>> query_headers()
        {'Content-Type': 'application/x-www-form-urlencoded', 'new value': 1}

    """

    def __init__(self, data: dict[str, any] = None, **kwargs) -> None:
        """__init__

        Add data as an instance attribute if provided.
        Otherwise, initialize the object with ``data`` set to an empty dict.

        """

        data: dict[str, any] = data or dict()
        data.update(kwargs)
        self.data_list: list[str] = []
        for k, v in data.items():
            setattr(self, k, v)
            self.data_list.append(k)

    def __call__(self, **extra: dict[str, any]) -> dict[str, any]:
        """__call__

        Retrieve the instance's data. If additonal kwargs are provided,
        return those values updated with the instance's data instead.

        Example::

            >>> from halo_psa.utils import BaseData
            >>> content_type = BaseData(
            >>>     {"Content-Type": "application/x-www-form-urlencoded"}
            >>> )
            >>> content_type()
            {'Content-Type': 'application/x-www-form-urlencoded'}

        """
        data = {key: self.get(key) for key in self.data_list}
        data.update(extra)
        return data

    def add(self, name: str, value: any) -> None:
        """add

        Add new data to the instance.

        Args:
            name (str): The data's name
            value (str): The data's value
        """
        self.data_list.append(name)
        setattr(self, name, value)

    def list_options(self) -> list[str]:
        """list_options

        Get a list of data available in the instance.

        Returns:
            list[str]: Data keys
        """
        return self.data_list

    def get(self, name: str) -> str:
        """get

        Get data values from the instance.

        Args:
            name (str): The data's name

        Returns:
            str: The data's value
        """
        return getattr(self, name)
