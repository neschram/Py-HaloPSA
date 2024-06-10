"""core.validators

Validation methods for the pyHaloPSA package.

Attrs:
    check_response
    ValidateAuthToken

"""

from datetime import datetime
from requests import Response
from .exceptions import RequestDenied, TokenExpired


def check_response(resp: Response, **kwds) -> None:
    """check_response

    Validates a request's response status is acceptable.
    If not, raise a RequestDenied exception.

    Args:
        resp (Response): The response data to validate

    Raises:
        RequestDenied: The request did not return a 200 status code.
    """
    if resp.status_code != 200:
        msg: str = kwds.pop("msg", f"{resp.status_code}: {resp.reason}")
        raise RequestDenied(msg, request=resp.request)


class ValidateAuthToken:
    """ValidateToken

    Validates an authentication token is still active.
    """

    def __init__(self, expires: datetime):
        if expires < datetime.now():
            raise TokenExpired(f"token expired on {expires}")
