from typing import NamedTuple

from ._config import Config
from ._request import Request


class GuestAPI(NamedTuple):
    config: Config = Config()

    def request_link(self, email: str) -> Request[bool]:  # pragma: no cover
        return Request(
            method='POST',
            url=f'{self.config.auth_url}/magic-link',
            headers={
                'authorization': 'Basic ODQ3MzYyMzAxMDpaTUhaM1RZT1pIVUxFRlhMUDRRQ1BIV0k1RDNWQVpNNw==',
                **self.config.headers,
            },
            data={'email': email},
            on_status=lambda status: status == 202,
        )

    def get_token(self, magic_link: str) -> Request[str]:  # pragma: no cover
        magic_link = magic_link.split('/')[-1]
        return Request(
            method='POST',
            url=f'{self.config.auth_url}/authorize',
            headers={
                'authorization': 'Basic ODQ3MzYyMzAxMzpHRFNTS1ozUU5RQ081QkNXN0RJRFhVWEE2RENSUUNNRQ==',
                **self.config.headers,
            },
            data={
                'credentials': {'token': magic_link},
                'type': 'magiclink',
            },
            on_json=lambda data: data['access_token'],
        )
