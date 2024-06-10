from datetime import datetime


class AuthToken:
    EXPIRES: datetime = datetime(2000, 1, 1, 0, 0, 1)
    TOKEN_TYPE: str = "Bearer"
    ACCESS_TOKEN: str = None

    def __call__(self) -> str:
        return f"{self.TOKEN_TYPE} {self.ACCESS_TOKEN}"
