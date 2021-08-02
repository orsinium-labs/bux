from typing import List
from ._response import Response
from ._price import Price
from ._filter import Filter
from ._security import Security


class SecurityMover(Security):
    @property
    def country_code(self) -> str:
        return self._sec['countryCode']

    @property
    def today_low(self) -> Price:
        return Price(self['stats']['todayLow'])

    @property
    def today_high(self) -> Price:
        return Price(self['stats']['todayHigh'])


class Movers(Response):
    @property
    def toggle_filters(self) -> List[Filter]:
        return [Filter(f) for f in self['filters']['toggleFilters']]

    @property
    def value_filters(self) -> List[Filter]:
        return [Filter(f) for f in self['filters']['valueFilters']]

    @property
    def gainers(self) -> List[SecurityMover]:
        return [SecurityMover(s) for s in self['gainers']]

    @property
    def losers(self) -> List[SecurityMover]:
        return [SecurityMover(s) for s in self['losers']]
