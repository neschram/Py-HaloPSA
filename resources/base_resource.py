import requests
from auth import HaloAuth
from utils import BaseData


class BaseResource(HaloAuth):

    def __init__(self, query_params: BaseData = BaseData(), **extra):
        self._query_params: BaseData = query_params
        super().__init__(**extra)

    def get_resources(self):
        return requests.get(
            url=self.page, headers=self.query_headers, data=self.query_params
        ).json()

    @property
    def query_params(self) -> dict[str, any]:
        return self._query_params()

    @query_params.setter
    def query_params(self, params: dict[str, any]) -> None:
        for k, v in params.items():
            self._query_params.add(k, v)
