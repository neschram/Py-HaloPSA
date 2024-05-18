# 3rd party
from decouple import config

BASE_URL: str = config("BASE_URL")
AUTH_URL: str = f"{BASE_URL}/{config('AUTH_URL')}/token"
RESOURCE_SERVER: str = f"{BASE_URL}/{config('RESOURCE_SERVER')}"
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
