from typing import Dict, List, NamedTuple

from . import types
from ._config import Config
from ._request import Request
from ._securities import Securities
from ._security import Security


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

    def authorize(self, pin: str) -> Request[str]:  # pragma: no cover
        """Request access token.

        Access token is not currently required to work with any endpoints.
        Expires after 10 minutes.
        `pin` is the PIN code that the app asks you on log in.
        """
        assert pin.isdigit()
        assert len(pin) == 5
        return Request(
            method='POST',
            url=f'{self.config.stocks_url}/authorization/13/users/me/authorize',
            body=pin.encode(),
            headers=self._headers,
            on_json=lambda x: x['access_token'],
        )

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
        """Get information about stocks you follow.
        """
        return Request(
            url=f'{self.config.stocks_url}/market-query/13/users/me/following',
            headers=self._headers,
            on_json=types.Following,
        )

    def inbox(self) -> Request[List[types.Message]]:
        return Request(
            url=f'{self.config.stocks_url}/inbox-query/13/users/me/inbox',
            headers=self._headers,
            on_json=lambda data: [types.Message(m) for m in data],
        )

    def tikkie_deposit(self, amount: int, *, currency: str = 'EUR') -> Request[str]:
        """Request tikkie payment URL.
        """
        return Request(
            method='POST',
            url=f'{self.config.stocks_url}/payment-query/13/payment/tikkie/deposit',
            headers=self._headers,
            data=dict(
                amount=f'{amount}.00',
                currency=currency,
                decimals=2,
            ),
            on_json=lambda data: data['paymentUrl'],
        )

    def search(self, query: str) -> Request[types.Search]:
        return Request(
            url=f'{self.config.stocks_url}/market-query/13/search',
            headers=self._headers,
            params=dict(q=query),
            on_json=types.Search,
        )

    def security(self, id: str) -> Security:
        """Get security-specific API
        """
        return Security(api=self, id=id)

    def securities(self) -> Securities:
        """Get securities-specific API
        """
        return Securities(api=self)
