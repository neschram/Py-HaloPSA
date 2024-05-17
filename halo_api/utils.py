import requests
import json


class GET:

    _url: str = ...
    _headers: dict[str, str] = ...
    _params: dict[str, str] = {}

    def __init__(
        self, url: str, headers: dict[str, str], auth: dict[str, str], **kwargs
    ) -> requests:
        self._url: str = url
        self._headers: dict[str, str] = headers
        self._auth: dict[str, str] = auth
        if kwargs:
            for k, v in kwargs:
                self._params[k] = v

    @staticmethod
    def _decode_response(response):
        """_decode_response

        Creates a python dictionary from the response text.

        If there is an error in the call, raise a ValueError citing the stauts code and reason.
        """
        if response.status_code == 200:  #: check for success
            return json.loads(response.text)
        raise ValueError(f"{response.status_code}: {response.reason}")

    def _raw_data(
        self,
        pk: int = None,
        extra_headers: dict[str, str] = None,
        query: dict[str, str] = None,
    ) -> dict[str, str]:
        """get(self, pk, extra_headers, query)

        call an API GET request

        Args:
            pk (int, optional): id of object. Defaults to None.
            extra_headers (dict[str, str], optional): additional headers.
            Defaults to None.
            query (dict[str, str], optional): additional parameters.
            Defaults to None.

        Returns:
        dict[str, str]: response data
        """

        # set the url
        url = self._url
        if pk is not None:
            url += f"/{pk}"

        # set the headers
        headers = self._headers
        if extra_headers is not None:
            headers.update(extra_headers)

        # set the query parameters
        params = self._params
        if query is not None:
            params.update(query)

        # finally, send the GET request
        return requests.get(
            url=self._url,
            params=params,
            headers=headers,
        )

    def all(
        self,
        extra_headers: dict[str, str] = None,
        query: dict[str, str] = None,
    ) -> dict[str, str]:
        return self._decode_response(
            self._raw_data(extra_headers=extra_headers, query=query)
        )
