from dataclasses import dataclass, field
from typing import Dict, Tuple, List, Any
from requests import request, Response
from .utils import Param, build_url


@dataclass
class Resource:

    query_params: List[Param]
    page: str
    container: str = field(default="")
    pk_field: str = field(default="id")
    name_field: str = field(default="name")

    @property
    def query_options(self):
        return [p.name for p in self.query_params]

    @property
    def url(self) -> str:
        return build_url(self.page)

    def _build_query_params(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        """_build_query_params

        Compiles a dictionary to pass to the requests module as parameters.

        Returns:
            dict[str, Any]: a dictionary of query parameters
        """
        outdata: Dict[str, Any] = dict()
        for param in self.query_params:
            if param.value is not None:
                outdata.update({param.name: param.value})
        outdata.update(kwargs)
        return outdata

    def request_context(
        self,
        **kwargs: Dict[str, Any],
    ) -> Tuple[str, Dict[str, Any]]:
        """request_context

        Returns the API page and the query parameters of the resource.

        Returns:
            Tuple[str, Dict]: page, _build_query_params
        """
        return self.page, self._build_query_params(**kwargs)

    def _get(self, auth, **kwargs) -> Dict[str, Any]:
        resp: Response = request(
            method="get",
            url=self.url,
            headers=auth,
            params=self._build_query_params(**kwargs)
        )
        rdata: Dict[str, Any] = resp.json()
        if self.container not in [None, ""]:
            rdata = rdata[self.container]

    def list_all(self, auth, **kwargs) -> List[str]:
        outdata: List[str] = list()
        for x in self._get(auth, **kwargs):
            outdata.append(f"{x[self.pk_field]}: {x['name']}")
        return outdata
