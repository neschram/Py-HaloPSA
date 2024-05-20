# halo_api/resource/__init__.py

"""
The `resources` module consists of HaloPSA API Resources as defined by the
HaloPSA API documentation:

    https://haloservicedesk.com/apidoc/resources

Each module consists of a separate Resource containing an instance of:

    :class:`halo_api.resources.base.BaseResource`
    and
    :class:`halo_api.resources.base.ResourceInstance`

Creating a Resource
-------------------

Resource Location
^^^^^^^^^^^^^^^^^

New Resources should be created in their own self_titled file.

    For example, the Client resource lives at `halo_api/resources/clients.py`.

Resource Class
^^^^^^^^^^^^^^

The Resource should subclass
    :class:`halo_api.resources.base.BaseResource`.

Resource Instances should  subclass
    :class:`halo_api.resources.base.ResourceInstance`.

Take the clients resource module for example::

    # halo_psa/resources/clients.py

    from halo_api.resources.base import BaseResource, ResourceInstance

    class ClientInstance(ResourceInstance):
        INSTANCE_NAME: str = "Client"
        INSTANCE_FIELD_NAMES: list[str] = ["id", "name", "colour"]

    class ClientResource(BaseResource):
        ...
        INSTANCE_CLASS: Instance = ClientInstance

Adding the Resource
-------------------

Once finished, import the module into `halo_api/resources/__init__.py`
and add it to `RESOURCE_LIST`.

Again, let's reference the clients module::

    # halo_psa/resources/__init__.py

    from .clients import ClientResource
    ...
    RESOURCE_LIST: list[BaseResource] = [
        ...
        ClientResource,
    ]
    ...
"""

# local
from .base import BaseResource
from .clients import ClientResource

# -- Resource List -----
# Add your imported Resource to this list

RESOURCE_LIST: list[BaseResource] = [
    ClientResource,
]  #: HaloPSA API Resources for the Resource class.


# -- Resource -----
# The Resource class that will be imported into the API module.

# -------------------------------------------------------------
#       This class should not be modified for the sake of
#                      an imported Resource.
# -------------------------------------------------------------


class Resource:
    """Resource

    A wrapper class for managing API endpoints for
    HaloPSA API Resources.

    .. warning::

        This class should not be altered to accomodate
        the features of a single `BaseResource` instance.

    Raises:
        KeyError: No resource found

    Returns:
        BaseResource: The API Resource object
    """

    # Add HaloPSA API Resources
    RESOURCES: dict[str, BaseResource] = {
        resource.RESOURCE_NAME: resource for resource in RESOURCE_LIST
    }  #: name the resources for lookups

    # Create the __call__ method for easier access
    def __call__(self, resource: str) -> BaseResource:
        """__call__

        Calls a HaloPSA API Resource object.

        Args:
            resource (str): The resource's RESOURCE_NAME

        Example ::

            >>> Resource("Client")
            <class: halo_api.resources.clients.ClientResource>

        """
        return getattr(self, resource)()

    # Assign the return string for the Resource class
    def __str__(self) -> str:
        title: str = "HaloPSA Resource"
        options: str = "\n- ".join([k for k in self.RESOURCES.keys()])
        return "\n".join(
            [title, "-" * len(title), "options include:", options]
        )

    # Assign the call string for the Resource class
    def __repr__(self) -> str:
        return f"HaloPSA.Resource(resource_list={self.resource_list})"

    def __init__(self) -> None:
        for resource in RESOURCE_LIST:
            setattr(self, resource.RESOURCE_NAME, resource)

    def list_resources(self):
        return [r.RESOURCE_NAME for r in RESOURCE_LIST]
