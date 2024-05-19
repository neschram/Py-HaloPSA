"""halo_api/settings.py

Default settings for the Py-HaloPSA project.

Do not set your settings from this file. Instead,
Use a configuration file (`.env`) or environment variables
to store the following settings:

Configuration Settings:

    BASE_URL (str): The base path to your API.
    Do not add a trailing slash ("/").
    Example, "https://support.haloservicedesk.com".
    AUTH_PAGE (str): the authentication page. Typically,
    this value will be "auth".
    ACTION_PAGE (str): The API's base query page. Typically,
    this value will be "api".
    TENANT (str): Your HaloPSA tenant name.
    CLIENT_ID (str): The client ID of your
    HaloPSA integration app.
    CLIENT_SECRET (str): The client secret of your
    HaloPSA integration app.
    SCOPE (str): Authentication scopes or privileges.
    As far as I have been able to discern, this will not work.
    Keep the value set to "all".
    CONTENT_TYPE (str): The API Content-Type header.
    Defaults to "application/x-www-form-urlencoded".
    GRANT_TYPE (str): The API Authentication type.
    Defaults to "client_credentials".

Computed Settings Values:

    AUTH_URL (str): a full url pointing to the
    API's authentication path.
    RESOURCE_SERVER (str): a full url pointing to the
    API's resource query path.

"""

# 3rd party
from decouple import config

AUTH_URL: str = f"{config('BASE_URL')}/{config('AUTH_PAGE')}"
RESOURCE_SERVER: str = f"{config('BASE_URL')}/{config('ACTION_PAGE')}"
TENANT: str = config("TENANT")
CLIENT_ID: str = config("CLIENT_ID")
CLIENT_SECRET: str = config("CLIENT_SECRET")
SCOPE: str = config("SCOPE")
GRANT_TYPE: str = config(
    "GRANT_TYPE",
    default="client_credentials",
)
CONTENT_TYPE: str = config(
    "CONTENT_TYPE",
    default="application/x-www-form-urlencoded",
    cast=str,
)
