import os
from typing import TYPE_CHECKING, NamedTuple, Optional

from . import types
from ._request import Request


if TYPE_CHECKING:
    from ._user import UserAPI


class Security(NamedTuple):
    api: 'UserAPI'
    id: str

    def follow(self) -> Request[bool]:
        return Request(
            method='PUT',
            url=f'{self.api.config.stocks_url}/market-presentation/13/users/me/following/stocks/{self.id}',
            headers=self.api._headers,
            on_status=lambda status: status == 202,
        )

    def unfollow(self) -> Request[bool]:
        return Request(
            method='DELETE',
            url=f'{self.api.config.stocks_url}/market-presentation/13/users/me/following/stocks/{self.id}',
            headers=self.api._headers,
            on_status=lambda status: status == 202,
        )

    def presentation(self) -> Request[types.SecurityPresentation]:
        return Request(
            url=f'{self.api.config.stocks_url}/market-presentation/13/product/securities/{self.id}',
            headers=self.api._headers,
            on_json=types.SecurityPresentation,
        )

    def stats(self) -> Request[types.SecurityStats]:
        return Request(
            url=f'{self.api.config.stocks_url}/product-stats/13/stats/{self.id}',
            headers=self.api._headers,
            on_json=types.SecurityStats,
        )

    def graph(self, type: str = '1d') -> Request[types.SecurityGraph]:
        return Request(
            url=f'{self.api.config.stocks_url}/market-query/13/securities/{self.id}/graph/price?type={type}',
            headers=self.api._headers,
            on_json=types.SecurityGraph,
        )

    def orders_config(self, *, direction: str = 'BUY') -> Request[types.OrdersConfig]:
        assert direction in ('BUY', 'SELL')
        return Request(
            url=f'{self.api.config.stocks_url}/portfolio-query/13/users/me/ordersConfiguration',
            params=dict(
                isin=self.id,
                direction=direction,
            ),
            headers=self.api._headers,
            on_json=types.OrdersConfig,
        )

    def order(
        self, *,
        direction: str = 'BUY',
        quantity: int = 1,
        type: str = 'BASIC',
        fee: Optional[types.Price] = None,
    ) -> Request[types.OrdersConfig]:  # pragma: no cover
        assert direction in ('BUY', 'SELL')
        assert type in ('BASIC', 'MARKET', 'LIMIT_ORDER_1D')
        if fee is None:
            fee = types.Price(dict(
                amount='0.00',
                currency='EUR',
                decimals=2,
            ))
        if os.environ.get('BUX_SAFE'):
            raise RuntimeError('BUX_SAFE is set, cannot order')
        return Request(
            url=f'{self.api.config.stocks_url}/portfolio-presentation/13/users/me/orders',
            method='POST',
            data=dict(
                direction=direction,
                feeEstimate=dict(fee),
                isin=self.id,
                quantity=str(quantity),
                type=type,
            ),
            headers=self.api._headers,
            on_json=types.OrdersConfig,
        )
