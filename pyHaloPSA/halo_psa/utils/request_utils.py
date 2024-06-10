"""request_utils

Utilities to help facilitate API requests.
"""

import requests
from halo_psa.validators import Check


class GET:

    def __init__(
        self,
        endpoint: str,
        headers: dict[str, any],
        *args: list[any],
        **kwds: dict[str, any],
    ) -> None:
        self.response = None
        self.page: str = endpoint
        self._headers: dict[str, any] = headers
        self._params: dict[str, any] = kwds.pop("params", None)
        self._container: str = kwds.pop("data_group", None)
        if args:
            for arg in args:
                setattr(self, arg, arg)
        if kwds:
            for k, v in kwds:
                setattr(self, k, v)

    def _get_(self, **kwds: dict[str, any]) -> None:
        """_get

        The call to `requests.get()`

        Allows for updating default attributes.
        Before placing the request, specify url, params, and headers
        using values found in kwds or the default attribute for each.

        The response data is then stored in self._response to reduce
        the need for multiple calls to the API endpoint.

        Example::

            >>> ex_req = GET(
            >>>    endpoint="test",
            >>>    headers={"content-type": "text"}
            >>>    )
            >>> ex_req._get(
            >>>    "params"={"search": "foo"},
            >>>    "headers"=self.headers.update({"foo": "bar"}),
            >>> )
            >>> ex_request._response.reason
            'Not Found'

        """
        response: requests.Response = requests.get(
            url=kwds.pop("url", self.page),
            params=kwds.pop("params", self._params),
            headers=kwds.pop("headers", self._headers),
            **kwds,
        )
        Check.response_status(response)
        self.response = response

    def get(self, **kwds: dict[str, any]) -> dict:
        """get

        Return response data from a GET request
        """
        if kwds:  #: supplying kwds updates the response
            self._get_(**kwds)
        if self.response is None:
            self._get_(**kwds)
        return self.response.json()
