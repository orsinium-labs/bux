from ._config import Config
from ._promise import Promise
from typing import Dict, NamedTuple
from ._types import PersonalData, Me, Portfolio, Following


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

    def me(self) -> Promise[Me]:
        return Promise(
            method='GET',
            url=f'{self.config.stocks_url}portfolio-query/13/users/me',
            headers=self._headers,
            on_json=Me,
        )

    def personal_data(self) -> Promise[PersonalData]:
        return Promise(
            method='GET',
            url=f'{self.config.stocks_url}personal-data-service/13/user',
            headers=self._headers,
            on_json=PersonalData,
        )

    def portfolio(self) -> Promise[Portfolio]:
        return Promise(
            method='GET',
            url=f'{self.config.stocks_url}portfolio-query/13/users/me/portfolio',
            headers=self._headers,
            on_json=Portfolio,
        )

    def following(self) -> Promise[Following]:
        return Promise(
            method='GET',
            url=f'{self.config.stocks_url}market-query/13/users/me/following',
            headers=self._headers,
            on_json=Following,
        )
