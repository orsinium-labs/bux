from ._config import Config
from ._promise import Promise
from typing import Dict, NamedTuple


class Guest(NamedTuple):
    config: Config = Config()

    @property
    def _headers(self) -> Dict[str, str]:
        return {
            'authorization': f'Basic {self.config.token}',
            **self.config.headers,
        }

    def request_link(self, email: str) -> Promise[bool]:
        def callback(status: int):
            return status == 200
        return Promise(
            method='POST',
            url=f'{self.config.auth_url}magic-link',
            headers=self._headers,
            data={'email': email},
            on_status=callback,
        )

    def get_token(self, magic_link: str) -> Promise[str]:
        def callback(data: dict):
            assert data['token_type'] == 'Bearer'
            return data['access_token']
        magic_link = magic_link.split('/')[-1]
        return Promise(
            method='POST',
            url=f'{self.config.auth_url}magic-link',
            headers=self._headers,
            data={
                "credentials": {"token": magic_link},
                "type": "magiclink",
            },
            on_json=callback,
        )
