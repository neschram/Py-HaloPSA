# Py-HaloPSA

Python module for the HaloPSA API using Client Credentials from HaloPSA's HaloPSA API integration item.

## Documentation

No docs yet.

## Quick-Start

### Clone the repository and set up the environment

#### Environment Setup

1. `git clone git@github.com:neschram/Py-HaloPSA.git`
2. `cd Py-HaloPSA`
3. `python -m venv env`
4. `. env/bin/actinvate` or `.\env\Scripts\activate`
5. `python -m pip install -r requirements.txt`

#### Config file Setup

1. `cp .env.template .env`
2. Open the `.env` file and update it with your API information

#### Import the API module into your project

1. `from halo_api import HaloPSA`

#### Interact with resources

- `clients = HaloPSA.get("clients")`
- `agents = HaloPSA.get("agents")`
- `HaloPSA.lookup("agents", "Jane")`
- `HaloPSA.lookup("clients", "Sandboxed Thoughts")`
