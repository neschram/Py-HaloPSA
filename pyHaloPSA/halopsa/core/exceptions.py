from requests.exceptions import HTTPError


class RequestDenied(HTTPError):
    """The request did not receive an OK status"""


class TokenExpired(ValueError):
    """TokenExpired

    Value error signifying that the expiration date
    of an AuthToken object has passed.
    """
