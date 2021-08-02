from typing import Dict, NamedTuple

from ._config import Config
from ._request import Request
from ._security import Security
from ._securities import Securities
from . import types


class UserAPI(NamedTuple):
    token: str
    config: Config = Config()

    @property
    def _headers(self) -> Dict[str, str]:
        return {
            'authorization': f'Bearer {self.token}',
            'pin-authorization': 'Bearer null',
            **self.config.headers,
        }

    def me(self) -> Request[types.Me]:
        return Request(
            url=f'{self.config.stocks_url}/portfolio-query/13/users/me',
            headers=self._headers,
            on_json=types.Me,
        )

    def personal_data(self) -> Request[types.PersonalData]:
        return Request(
            url=f'{self.config.stocks_url}/personal-data-service/13/user',
            headers=self._headers,
            on_json=types.PersonalData,
        )

    def portfolio(self) -> Request[types.Portfolio]:
        return Request(
            url=f'{self.config.stocks_url}/portfolio-query/13/users/me/portfolio',
            headers=self._headers,
            on_json=types.Portfolio,
        )

    def following(self) -> Request[types.Following]:
        return Request(
            url=f'{self.config.stocks_url}/market-query/13/users/me/following',
            headers=self._headers,
            on_json=types.Following,
        )

    def security(self, id: str) -> Security:
        """Get security-specific API
        """
        return Security(api=self, id=id)

    def securities(self) -> Securities:
        """Get securities-specific API
        """
        return Securities(api=self)
