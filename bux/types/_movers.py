from typing import List
from ._response import Response
from ._price import Price
from ._filter import Filter


class SecurityMover(Response):
    @property
    def bid(self) -> Price:
        return Price(self['bid'])

    @property
    def closing_bid(self) -> Price:
        return Price(self['closingBid'])

    @property
    def country_code(self) -> str:
        return self['countryCode']

    @property
    def description(self) -> str:
        return self['description']

    @property
    def id(self) -> str:
        return self['id']

    @property
    def name(self) -> str:
        return self['name']

    @property
    def security_type(self) -> str:
        return self['securityType']

    @property
    def today_low(self) -> Price:
        return Price(self['stats']['todayLow'])

    @property
    def today_high(self) -> Price:
        return Price(self['stats']['todayHigh'])

    @property
    def offer(self) -> Price:
        return Price(self['offer'])

    @property
    def opening_bid(self) -> Price:
        return Price(self['openingBid'])

    @property
    def ticker_code(self) -> str:
        return self['tickerCode']


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
