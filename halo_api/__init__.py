from halo_api.core.auth import HaloAuth
from halo_api.resources import Resource


class HaloPSA(HaloAuth):

    def __init__(self, connect_on_init: bool = False, **extra):
        super().__init__(**extra)
        if connect_on_init:
            self.connect()

    def __call__(self, resource: str) -> Resource:
        return getattr(Resource, resource)

halo: HaloPSA = HaloPSA()