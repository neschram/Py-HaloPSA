import datetime


class TokenExpired(ValueError):
    """TokenExpired

    Value error signifying that the expiration date
    of an AuthToken object is expired.
    """


class ValidateAuthToken:
    """ValidateToken

    Validates an authentication token is still active.
    """

    def __init__(self, expires: datetime):
        if expires < datetime.now():
            raise TokenExpired(f"token expired on {expires}")
