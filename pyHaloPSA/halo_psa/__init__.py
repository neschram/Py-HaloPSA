from typing import Dict
from .auth import Auth
from . import query_params as Q
from .resources import Resource


class HaloAPI:
    _auth: Auth = Auth()

    clients: Resource = Resource(
        query_params=[
            Q.Pageinate(value=False),
            Q.PageSize(value=10000),
            Q.PageNo(),
            Q.Order(value="name"),
            Q.OrderDesc(value=False),
            Q.Search(),
            Q.ToplevelID(),
            Q.IncludeInactive(value=True),
            Q.IncludeActive(value=True),
            Q.Count(value=10000),
        ],
        page="Client",
        container="clients",
        pk_field="id",
    )

    @property
    def auth(self) -> Dict[str, str]:
        """auth

        A simple way to ensure that the object
        has authenticated against the HaloPSA API and
        get the authorization headers for API calls.

        Returns:
            Dict[str, str]: authorization headers
        """
        return self._auth.credentials
