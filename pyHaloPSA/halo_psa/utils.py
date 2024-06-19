# core/utils.py

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List
import requests
from datetime import datetime, timedelta
from requests import Response
from .exceptions import ResponseError
from .settings import RESOURCE_SERVER


def dress_data(data: Dict[str, Any]) -> str:
    """dress_data

    Prepares a dictionary for a POST request by:

    1. Wrapping the dictionary in a list
    2. Reformatting the list with :func:`json.dumps()`

    Args:
        data (dict[str, any]): The data to dress for a POST request

    Returns:
        str: The dressed data

    Example:
        >>> data = {"a": 1, "b": "two", "c": False}
        >>> dress_data(data)
        '[{"a": 1, "b": "two", "c": False}]'

    """
    return json.dumps([data])


def validate_response(response: Response) -> None:
    status: int = response.status_code
    reason: str = response.reason

    if status != 200:
        raise ResponseError(f"{status}: {reason}")


def check_for_pk(field: str, data: Dict[str, Any]) -> None:
    """check_for_pk

    Check that the field exists and is not None in data

    Args:
        field (str): Name of the field
        data (dict[str, any]): Data to look in

    Raises:
        ValueError: The field doesn't exist
        ValueError: The field value is None
    """
    if field in data:
        if data[field] is None:
            raise ValueError(field, "field cannot be empty")
    raise ValueError(field, "field cannot be empty")


def is_recent(
    last_update: datetime,
    timeframe: timedelta = timedelta(minutes=30)
) -> bool:
    check_time: datetime = datetime.now() - timeframe
    return check_time < last_update


def build_url(page: str, pk: int | None = None, base: str = RESOURCE_SERVER) -> str:
    """build_url

    Compiles a web address for the an API call.

    Args:
        page (str): The resource's page name
        pk (int | None, optional): An optional Resource Record ID. Defaults to None.
        base (str, optional): The base URL of the API address. Defaults to RESOURCE_SERVER.

    Returns:
        str: A full HTTP web address for the API request.
    """
    base_url: str = f"{base}/{page}"
    if pk is not None:
        base_url += f"/{pk}"
    return base_url


class GET:

    def __init__(
        self, url: str,
        headers: Dict[str, Any],
        params: Dict[str, Any],
        send: bool = False,
        last_update: datetime = datetime(
            2000, 1, 1, 0, 0, 1
        )
    ) -> None:

        self.url: str = url
        self.headers: Dict[str, Any] = headers
        self.params: Dict[str, Any] = params
        self.response: Response | None = None
        self.last_update = last_update
        if send:
            self._send_request(self.url, self.headers, params=self.params)

    def _send_request(
        self,
        url: str,
        headers: Dict[str, str] | None,
        **params: Dict[str, Any] | None,
    ) -> None:
        """GET

        Initiates a :func:`requests.get()` call to the HaloPSA API endpoint.
        """
        response: Response = requests.get(
            url=url, headers=headers, params=params
        )
        validate_response(response)
        self.response = response

    def __call__(self, params: Dict[str, Any]) -> Response | None:
        if params == self.params and is_recent(self.last_update):
            return self.response
        self.params.update(params)
        self._send_request(self.url, self.headers, **self.params)
        return self.response


class POST:

    def __init__(
        self,
        url: str,
        headers: Dict[str, str],
        data: Dict[str, Any],
        send: bool = False,
    ) -> None:
        self.url: str = url
        self.headers: Dict[str, Any] = headers
        self. data: Dict[str, Any] = data
        if send:
            self._send_request(
                self.url,
                self.headers,
                self.data,
            )

    def _send_request(
        self,
        url: str,
        headers: Dict[str, str],
        data: Dict[str, Any],
    ) -> None:
        """POST

        Initiates a :func:`requests.post()` call to the HaloPSA API endpoint
        """
        response: Response = requests.post(
            url=url,
            headers=headers,
            data=data,
        )
        validate_response(response)
        self.response: Response = response

    def __call__(self, data: Dict[str, Any] = dict()) -> Response:
        self.data.update(data)
        self._send_request(self.url, self.headers, self.data)
        return self.response


class DataDict:

    def __init__(self, **kwargs) -> None:
        self.__fields__: list[str] = list()
        if kwargs:
            for k, v in kwargs.items():
                self.__fields__.append(k)
                setattr(self, k, v)

    def get(self, name: str) -> Any:
        try:
            return getattr(self, name)
        except AttributeError:
            raise AttributeError(name, "Field not found")

    def encode(self) -> str:
        data_dict: Dict[str, Any] = dict()
        for attr in self.__fields__:
            data_dict[attr] = getattr(self, attr)
        return dress_data(data_dict)


@dataclass
class Param:
    """Param

    A request parameter available for HaloPSA Resources.

    Attrs:
        name (str): The parameter's name as listed in
        HaloPSA's API documentation.
        param_type (str): The parameter type as listed in
        HaloPSA's API documentation.
        data_type (type): The python datatype of the instances :attr:`value`.
        description (str): The parameter description.
        It is advised to use HaloPSA's provided parameter description.
        value (Any, optional): The value to pass in an API call.
        Defaults to None.

    Example:
        >>> from halo_psa.resources.params.base_parameters import Param
        >>> test_param = Param(
        >>>     name: str = "test_param",
        >>>     param_type: str = "query",
        >>>     data_type: type = bool,
        >>>     description: str = "an example Param",
        >>>     value: any = False,
        >>> )
        >>> test_param.value
        False
        >>> test_param.param_type
        "query"
        >>> test_param
        Param(
            name="test_param",
            param_type="query",
            data_type=<class 'bool'>,
            description="an example Param",
            value=False
        )

    """

    name: str
    """The parameter's name as listed in HaloPSA's API documentation."""
    param_type: str
    """The parameter type as listed in HaloPSA's API documentation."""
    data_type: type
    """The python datatype of the instances :attr:`value`."""
    description: str
    """The parameter description. It is advised to use HaloPSA's
    provided parameter description.
    """
    value: Any = None
    """The value to pass in an API call. Defaults to None."""

    def _validate_value(self) -> None:
        if (
            self.value is not None
        ) and (
            type(self.value) is not self.data_type
        ):
            raise AttributeError(
                self.value,
                f"value must be of type {self.data_type}",
            )

    def __post_init__(self):
        """__post_init__

        Calls :func:`self._validate_value()` after class initializaiton to
        validate that the type of self.value matches self.data_class or None
        """
        self._validate_value()

    def _build_param(self) -> dict[str, Any]:
        """_build_param

        Returns:
            dict[str, Any]: Returns a dictionary of {self.name: self.value}
        """
        return {self.name: self.value}

    @property
    def param(self):
        return self._build_param()

    @param.setter
    def param(self, value):
        self.value = value


@dataclass
class Resource:

    query_params: List[Param]
    page: str
    container: str | None = field(default=None)
    pk_field: str = field(default="id")

    @property
    def query_options(self):
        return [p.name for p in self.query_params]

    def _build_query(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        """_build_query

        Compiles a dictionary to pass to the requests module as parameters.

        Returns:
            dict[str, Any]: a dictionary of query parameters
        """
        outdata: dict[str, Any] = dict()
        for param in self.query_params:
            if param.value is not None:
                outdata.update({param.name: param.value})
        outdata.update(kwargs)
        return outdata

    def request_context(self, **kwargs: dict[str, Any]) -> tuple[str, dict]:
        """request_context

        Returns:
            tuple[str, dict]: page, _build_query
        """
        return self.page, self._build_query(**kwargs)


@dataclass
class Record:
    pk_field: str = field(default="id", kw_only=True)
    name_field: str = field(default="name", kw_only=True)

    def __str__(self) -> str:
        pk: int = getattr(self, self.pk_field)
        name: str = getattr(self, self.name_field)
        return f"Record #{pk}: {name}"
