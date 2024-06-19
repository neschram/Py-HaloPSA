"""
Config.Settings
===============

Default settings for the Py-HaloPSA project.

Do not set your settings from this file. Instead,
Use a configuration file (`.env`) or environment variables
to store the following settings:

Configuration Settings:
-----------------------

    BASE_URL (str):
        The base path to your API. Do not add a trailing slash ("/").
        Example:
            "https://support.haloservicedesk.com".
    TENANT (str):
        Your HaloPSA tenant name.
    CLIENT_ID (str):
        The client ID of your HaloPSA integration app.
    CLIENT_SECRET (str):
        The client secret of your HaloPSA integration app.
    AUTH_PAGE (str):
        The authentication page.
        Defaults to "auth".
    ACTION_PAGE (str):
        The API's base query page.
        Defaults to "api".
    SCOPE (str):
        Authentication scopes or privileges.
        Defaults to "all".
    CONTENT_TYPE (str):
        The API Content-Type header.
        Defaults to "application/x-www-form-urlencoded".
    GRANT_TYPE (str):
        The API Authentication type.
        Defaults to "client_credentials".

Attrs:
    AUTH_URL (str):
        A full url pointing to the API's authentication path.
    RESOURCE_SERVER (str):
        A full url pointing to the API's resource query path.
    TENANT (str):
        Your HaloPSA tenant name.
    CLIENT_ID (str):
        The client ID of your HaloPSA integration app.
    CLIENT_SECRET (str):
        The client secret of your HaloPSA integration app.
    AUTH_PAGE (str):
        The authentication page.
        Defaults to "auth".
    ACTION_PAGE (str):
        The API's base query page.
        Defaults to "api".
    SCOPE (str):
        Authentication scopes or privileges.
        Defaults to "all".
    CONTENT_TYPE (str):
        The API Content-Type header.
        Defaults to "application/x-www-form-urlencoded".
    GRANT_TYPE (str):
        The API Authentication type.
        Defaults to "client_credentials".


"""

# 3rd party
from decouple import config

# Base settings
BASE_URL: str = config("BASE_URL")
"""The base path to your API. Do not add a trailing slash ("/").

    Example:
        `'https://support.haloservicedesk.com'`
"""
TENANT: str = config("TENANT")
"""Your HaloPSA tenant name."""
CLIENT_ID: str = config("CLIENT_ID")
CLIENT_SECRET: str = config("CLIENT_SECRET")
SCOPE: str = config("SCOPE", default="all")
AUTH_PAGE: str = config("AUTH_PAGE", default="auth/token")
ACTION_PAGE: str = config("ACTION_PAGE", default="api")
GRANT_TYPE: str = config(
    "GRANT_TYPE",
    default="client_credentials",
)
CONTENT_TYPE: str = config(
    "CONTENT_TYPE",
    default="application/x-www-form-urlencoded",
    cast=str,
)

# Computed settings
AUTH_URL: str = f"{BASE_URL}/{AUTH_PAGE}"
RESOURCE_SERVER: str = f"{BASE_URL}/{ACTION_PAGE}"
