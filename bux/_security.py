
from typing import TYPE_CHECKING
from ._promise import Promise
from typing import NamedTuple
from .types import SecurityStats, SecurityPresentation, SecurityGraph


if TYPE_CHECKING:
    from ._user import UserAPI


class Security(NamedTuple):
    api: 'UserAPI'
    id: str

    def presentation(self) -> Promise[SecurityPresentation]:
        return Promise(
            url=f'{self.api.config.stocks_url}market-presentation/13/product/securities/{self.id}',
            headers=self.api._headers,
            on_json=SecurityPresentation,
        )

    def stats(self) -> Promise[SecurityStats]:
        return Promise(
            url=f'{self.api.config.stocks_url}product-stats/13/stats/{self.id}',
            headers=self.api._headers,
            on_json=SecurityStats,
        )

    def graph(self, type: str = '1d') -> Promise[SecurityGraph]:
        return Promise(
            url=f'{self.api.config.stocks_url}market-query/13/securities/{self.id}/graph/price?type={type}',
            headers=self.api._headers,
            on_json=SecurityGraph,
        )
