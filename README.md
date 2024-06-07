# Py-HaloPSA

Python module for the HaloPSA API using Client Credentials from HaloPSA's HaloPSA API integration item.

## Documentation

No docs yet.

## Quick-Start

### 1. Clone the repository and set up the environment

---

1. Clone the repository into your project:
  
    ```bash
    git clone git@github.com:neschram/Py-HaloPSA.git
    ```

2. Install the package:

    ```bash
    (venv): python -m pip install /path/to/Py-HaloPSA/.
    ```

### 2. Configuration

There are two options for configuring the module to your API.

[Option 1](#config-file):

> Create or update a [`python-decouple`](https://github.com/HBNetwork/python-decouple)
compatilble config file.

[Option 2](#environment-variables)

> Add the configuration to your system's environment variables

---

#### Config file

If you do not already have a `python-decouple` compatible config file,
follow these steps to create one. If you do already have a compatible config file,
add the content from step 2 into your existing document.

1. Create a file named `.env` in the root of your project.

2. Copy the contents of [pyHaloPSA/.env.template](./pyHaloPSA/.env.template) to your `.env` file.

3. Update the variables with your API's information

    - Optional variables are commented out with a `#`

#### Environment Variables

Add the following to your environment variables:

- `BASE_URL`: The base path to your API.

  - *example*: `"https://support.haloservicedesk.com"`

- `TENANT`: Your HaloPSA tenant name.

  - *example*: `haloservicedesk`

- `CLIENT_ID`: Your HaloPSA API's Client ID

- `CLIENT_SECRET`: Your HaloPSA API's Client Secret

---

## 3. Import the API module into your project

```python
from halo_api import Halo
```

## 4. Interact with API resources

```python
  >>> clients = Halo.get("clients")
  >>> Halo.lookup("clients", "Sandboxed Thoughts")
  >>> agents = Halo.get("agents")
  >>> Halo.lookup("agents", "Nate")
```
