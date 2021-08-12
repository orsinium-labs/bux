
from typing import TYPE_CHECKING, NamedTuple

from ._request import Request
from .types import SecurityGraph, SecurityPresentation, SecurityStats


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

    def presentation(self) -> Request[SecurityPresentation]:
        return Request(
            url=f'{self.api.config.stocks_url}/market-presentation/13/product/securities/{self.id}',
            headers=self.api._headers,
            on_json=SecurityPresentation,
        )

    def stats(self) -> Request[SecurityStats]:
        return Request(
            url=f'{self.api.config.stocks_url}/product-stats/13/stats/{self.id}',
            headers=self.api._headers,
            on_json=SecurityStats,
        )

    def graph(self, type: str = '1d') -> Request[SecurityGraph]:
        return Request(
            url=f'{self.api.config.stocks_url}/market-query/13/securities/{self.id}/graph/price?type={type}',
            headers=self.api._headers,
            on_json=SecurityGraph,
        )
