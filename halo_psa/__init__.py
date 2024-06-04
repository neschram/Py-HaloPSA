import requests
from halo_psa.auth import HaloAuth as Auth
from halo_psa.resources import Clients, Agents


class Halo:
    _auth = Auth()
    _clients = Clients()
    _agents = Agents()

    _RESOURCES: list[str] = [
        "clients",
        "agents",
    ]

    def get_resource(self, value: str) -> object:
        """get_resource

        Find the listed resource value.

        Args:
            value (str): Resource to lookup

        Raises:
            ValueError: Resource not in resources list

        Returns:
            object: The equivalent Halo resource attribute
        """
        if value in self._RESOURCES:
            return getattr(self, f"_{value}")
        raise ValueError(f"Resource ({value}) not found")

    def list_resources(self) -> list[str]:
        """list_resources

        Returns the list of resource names.
        """
        return self._RESOURCES

    def get(
        self,
        resource: str,
        pk: int = None,
        headers: dict = None,
        params: dict = None,
    ):
        """get

        Perform a resource GET request.

        Args:
            resource (str): The desired resource's name
            pk (int, optional): An id of a specific resource object.
            Defaults to None.
            headers (dict, optional): Request headers.
            Defaults to None.
            params (dict, optional): Request parameters.
            Defaults to None.

        Returns:
            dict | list: Response data.
        """
        r = self.get_resource(resource)
        self._auth.connect()
        auth = self._auth.query_headers
        return r.get(auth=auth, headers=headers, params=params, pk=pk)

    def lookup(self, resource: str, value: str) -> list[dict[str, any]]:
        """lookup

        Performs a get request with an additional 'search' parameter.

        Args:
            resource (str): The name of the desired HaloPSA Resource.
            value (str): A search string for the request.

        Returns:
            list[dict[str, any]]: response data.

        Example::

            >>> halo = Halo()
            >>> halo.lookup("agents", "Nate")
            [{'id': 3,
              'name': 'Nathaniel Schram',
              ...
            }]

        """
        return self.get(resource=resource, params={"search": value})