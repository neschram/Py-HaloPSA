from requests.exceptions import HTTPError


class RequestDenied(HTTPError):
    """The request did not receive an OK status"""
