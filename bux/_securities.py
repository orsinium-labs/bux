
from typing import TYPE_CHECKING, NamedTuple

from ._request import Request
from . import types


if TYPE_CHECKING:
    from ._user import UserAPI


class Securities(NamedTuple):
    api: 'UserAPI'

    def movers(self) -> Request[types.Movers]:
        return Request(
            method='POST',
            url=f'{self.api.config.stocks_url}/market-query/13/securities/movers',
            headers=self.api._headers,
            data=dict(
                filters=dict(
                    toggleFilters=[],
                    valueFilters=[],
                ),
            ),
            on_json=types.Movers,
        )
