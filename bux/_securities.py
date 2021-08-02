
from typing import List, TYPE_CHECKING, NamedTuple

from ._request import Request
from . import types


if TYPE_CHECKING:
    from ._user import UserAPI


class Securities(NamedTuple):
    api: 'UserAPI'

    @property
    def _url(self):
        return f'{self.api.config.stocks_url}/market-query/13/securities'

    def movers(self) -> Request[types.Movers]:
        return Request(
            method='POST',
            url=f'{self._url}/movers',
            headers=self.api._headers,
            data=dict(
                filters=dict(
                    toggleFilters=[],
                    valueFilters=[],
                ),
            ),
            on_json=types.Movers,
        )

    def featured_tags(self) -> Request[List[types.Tag]]:
        return Request(
            url=f'{self._url}/stocks/featuredTags',
            headers=self.api._headers,
            on_json=lambda tags: [types.Tag(t) for t in tags],
        )

    def countries(self) -> Request[List[types.Tag]]:
        return Request(
            url=f'{self._url}/countries',
            headers=self.api._headers,
            params=dict(sorting='ALPHABETICAL'),
            on_json=lambda tags: [types.Tag(t) for t in tags],
        )

    def etfs(self) -> Request[List[types.Security]]:
        return Request(
            url=f'{self._url}/etf',
            headers=self.api._headers,
            on_json=lambda d: [types.Security(etf) for etf in d['etfCuratedList']],
        )

    def usa(self) -> Request[List[types.Security]]:
        return Request(
            url=f'{self._url}/stocks/usa',
            headers=self.api._headers,
            on_json=lambda d: [types.Security(etf) for etf in d['usaCuratedStocksList']],
        )

    def filter_tag(self, tag: str, *, available_cash: bool = False) -> Request[types.TagMatches]:
        return Request(
            url=f'{self._url}/filter/tag/{tag}',
            headers=self.api._headers,
            params=dict(availableCashFilterEnabled=available_cash),
            on_json=types.TagMatches,
        )

    def filter_new(self) -> Request[types.TagMatches]:
        return Request(
            url=f'{self._url}/filter/newlyAdded',
            headers=self.api._headers,
            on_json=types.TagMatches,
        )
