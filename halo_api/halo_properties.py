# halo_api/halo_properties.py


import json
from requests import request
from .settings import CONTENT_TYPE, RESOURCE_SERVER


class HaloResource:

    @staticmethod
    def _build_params(*params) -> str:
        param_list: list = []
        for k, v in params.items():
            param_list.append(f"{k}={v}")
        return "&".join(param_list)

    @staticmethod
    def _decode_response(response):
        if response.status_code == 200:
            return json.loads(response.text)
        raise ValueError(f"{response.status_code}: {response.reason}")

    def _list_all(self, title: str = "name"):
        objs: list[dict] = self.get_all()
        if type(objs) is dict:
            objs = objs[self.list_value]
        listed_objs: list[str] = [f"{i['id']} - {i[title]}" for i in objs]
        return listed_objs

    def __init__(
        self,
        token: str,
        page: str,
        list_value: str,
        content_type: str = CONTENT_TYPE,
        params: dict[str, str] = dict(),
    ) -> None:
        self.token = token
        self.page: str = f"{RESOURCE_SERVER}/{page}"
        self.parameters: dict[str, str] = params or dict()
        self.content_type: str = content_type
        self.list_value = list_value

    def _build_headers(self, **kwargs) -> dict[str, str]:
        headers: dict[str, str] = {
            "Content-Type": self.content_type,
            "Authorization": self.token,
        }
        if kwargs:
            for k, v in kwargs.items():
                headers[k] = v
        return headers

    def get_raw_data(self, **headers):
        return request(
            "GET", url=self.page, headers=self._build_headers(**headers)
        )

    def get_all(self, **headers):
        return self._decode_response(self.get_raw_data(**headers))

    @property
    def all(self):
        return self._list_all()

    def get(self, pk: int | str) -> dict[str, str]:
        if type(pk) is str:
            for i in self.all:
                if str(pk) in str(i):
                    pk = int(i.split(" - ")[0])
        return self._decode_response(
            request(
                "GET", url=f"{self.page}/{pk}", headers=self._build_headers()
            )
        )


class Client(HaloResource):
    def __init__(
        self,
        token: str,
        page: str = "Client",
        list_value: str = "clients",
        content_type: str = CONTENT_TYPE,
        params: dict[str, str] = dict(),
    ) -> None:
        super().__init__(token, page, list_value, content_type, params)


class Agent(HaloResource):
    def __init__(
        self,
        token: str,
        page: str = "Agent",
        list_value: str = "agents",
        content_type: str = CONTENT_TYPE,
        params: dict[str, str] = dict(),
    ) -> None:
        super().__init__(token, page, list_value, content_type, params)


class Ticket(HaloResource):
    def __init__(
        self,
        token: str,
        page: str = "Tickets",
        list_value: str = "tickets",
        content_type: str = CONTENT_TYPE,
        params: dict[str, str] = dict(),
    ) -> None:
        super().__init__(token, page, list_value, content_type, params)

    def _list_all(self, title: str = "idsummary"):
        return super()._list_all(title)
