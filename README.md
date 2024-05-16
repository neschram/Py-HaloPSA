# Py-HaloPSA
Python module for the HaloPSA API

## Quick-Start
1. [recommended] create and activate your environment: `python -m vnev env && . env/bin/activate`
2. install requirements: `python -m pip install -r requirements.txt`
3. copy the configuration template to a new file, ".env"
4. Update the .env file with your API information created from a Client Credential API in HaloPSA
5. launch python
6. import the module: `from halo_api import haloPSA`
7. If all varialbles in your config file (.env) are correct, you will have authenticated on import.
8. Check by calling `haloPSA.logged_in`

## HaloPSA Resources
Halo lists each section of their site as a resource. Each resource spawns from the object `HaloResource` in [halo_properties](halo_api/halo_properties.py).

### HaloResource methods
There are a few methods that each resource inherits from `HaloResource`:

#### HaloResource.get_all()
Basic get request that returns a dictionary of available items.

#### HaloResource.all
Returns a list representation of "{id} - {lookup_value}" from HaloResource.get_all()

#### HaloResource.get(pk)
