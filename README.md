# Py-HaloPSA

Python module for the HaloPSA API using Client Credentials from HaloPSA's HaloPSA API integration item.

## Quick-Start

1. [recommended] create and activate your environment: `python -m vnev env && . env/bin/activate`
2. install requirements: `python -m pip install -r requirements.txt`
3. copy the configuration template, `.env.template` to `.env`
4. Update the .env file with your API information created from a Client Credential API in HaloPSA
5. launch python
6. import the module: `from halo_api import haloPSA`
7. If all variables in your config file (`.env`) are correct, you will have authenticated on import.
8. Check by calling `haloPSA.logged_in`

## haloPSA

The main object of the module. All calls to the API will stem from this. Remeber that haloPSA will attempt to authenticate on import.

## HaloPSA Resources

Halo lists each section of their site as a resource. Each resource spawns from the object `HaloResource` in [halo_properties](halo_api/halo_properties.py).

Most API calls will be inherited from this class
