# Py-HaloPSA

Python module for the HaloPSA API using Client Credentials from HaloPSA's HaloPSA API integration item.

## Documentation

Build the documentation locally using sphinx:

1. Enable your environment
2. Move into the `docs` directory
3. Build the docs `./make html`
4. Navigate to `path/to/docs/build/html/index.html` in your web browser

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

### Import the API module into your project

1. `from halo_api import halo`

#### Authenticate the api

1. `halo.connect()`

#### Interact with resources

1. `clients = halo.Clients`
2. `clients._get_all()`
3. `clients.INSTANCES`
