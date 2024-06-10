from requests import Response
from halo_psa.exceptions import RequestDenied


class Check:
    """Check

    Verification checks
    """

    @staticmethod
    def response_status(resp: Response) -> None:
        if resp.status_code not in range(200, 299):
            raise RequestDenied(f"{resp.status_code}: {resp.reason}")
