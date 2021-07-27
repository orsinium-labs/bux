from typing import Dict, NamedTuple

from ._config import Config
from ._request import Request
from ._security import Security
from .types import Following, Me, PersonalData, Portfolio


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

    def me(self) -> Request[Me]:
        return Request(
            url=f'{self.config.stocks_url}/portfolio-query/13/users/me',
            headers=self._headers,
            on_json=Me,
        )

    def personal_data(self) -> Request[PersonalData]:
        return Request(
            url=f'{self.config.stocks_url}/personal-data-service/13/user',
            headers=self._headers,
            on_json=PersonalData,
        )

    def portfolio(self) -> Request[Portfolio]:
        return Request(
            url=f'{self.config.stocks_url}/portfolio-query/13/users/me/portfolio',
            headers=self._headers,
            on_json=Portfolio,
        )

    def following(self) -> Request[Following]:
        return Request(
            url=f'{self.config.stocks_url}/market-query/13/users/me/following',
            headers=self._headers,
            on_json=Following,
        )

    def security(self, id: str) -> Security:
        return Security(api=self, id=id)
