from typing import List

from ._filter import Filter
from ._response import Response
from ._security import Security


class Movers(Response):
    @property
    def toggle_filters(self) -> List[Filter]:
        return [Filter(f) for f in self['filters']['toggleFilters']]

    @property
    def value_filters(self) -> List[Filter]:
        return [Filter(f) for f in self['filters']['valueFilters']]

    @property
    def gainers(self) -> List[Security]:
        return [Security(s) for s in self['gainers']]

    @property
    def losers(self) -> List[Security]:
        return [Security(s) for s in self['losers']]
