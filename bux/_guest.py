from typing import Dict, NamedTuple

from ._config import Config
from ._request import Request


class GuestAPI(NamedTuple):
    config: Config = Config()

    @property
    def _headers(self) -> Dict[str, str]:
        return {
            'authorization': f'Basic {self.config.token}',
            **self.config.headers,
        }

    def request_link(self, email: str) -> Request[bool]:
        def callback(status: int):
            return status == 200
        return Request(
            method='POST',
            url=f'{self.config.auth_url}/magic-link',
            headers=self._headers,
            data={'email': email},
            on_status=callback,
        )

    def get_token(self, magic_link: str) -> Request[str]:
        def callback(data: dict) -> str:
            assert data['token_type'] == 'Bearer'
            return data['access_token']
        magic_link = magic_link.split('/')[-1]
        return Request(
            method='POST',
            url=f'{self.config.auth_url}/authorize',
            headers=self._headers,
            data={
                "credentials": {"token": magic_link},
                "type": "magiclink",
            },
            on_json=callback,
        )
