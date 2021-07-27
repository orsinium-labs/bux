
from typing import TYPE_CHECKING, NamedTuple

from ._request import Request
from .types import SecurityGraph, SecurityPresentation, SecurityStats


if TYPE_CHECKING:
    from ._user import UserAPI


class Security(NamedTuple):
    api: 'UserAPI'
    id: str

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
