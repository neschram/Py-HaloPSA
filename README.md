# Py-HaloPSA

Python module for the HaloPSA API using Client Credentials from HaloPSA's HaloPSA API integration item.

## Quick-Start

1. [recommended] create and activate your environment: `python -m vnev env && . env/bin/activate`
2. install requirements: `python -m pip install -r requirements.txt`
3. copy the configuration template, `.env.template` to `.env`
4. Update the .env file with your API information created from a Client Credential API in HaloPSA
5. launch python
6. From here you can choose to load an available resource, `from halo_api import Clients`
or
import the base resource `from halo_api.base import HaloResource`

> [!Important]
> Resources will send a get request to load the respective data on import at this time.
> I plan to reduce this to a switch on init later, but for now, it makes my testing easier.
