from typing import List
from ._response import Response
from ._price import Price


class SecurityFollowing(Response):
    @property
    def bid(self) -> Price:
        return Price(self['security']['bid'])

    @property
    def closing_bid(self) -> Price:
        return Price(self['security']['closingBid'])

    @property
    def opening_bid(self) -> Price:
        return Price(self['security']['openingBid'])

    @property
    def country_code(self) -> str:
        return self['security']['countryCode']

    @property
    def description(self) -> str:
        return self['security']['description']

    @property
    def id(self) -> str:
        return self['security']['id']

    @property
    def name(self) -> str:
        return self['security']['name']

    @property
    def security_type(self) -> str:
        return self['security']['securityType']

    @property
    def offer(self) -> Price:
        return Price(self['security']['offer'])

    @property
    def ticker_code(self) -> str:
        return self['security']['tickerCode']

    @property
    def following(self) -> int:
        return self['socialInfo']['following']

    @property
    def followers(self) -> int:
        return self['socialInfo']['followers']


class Following(Response):
    @property
    def eqty(self) -> List[SecurityFollowing]:
        return [SecurityFollowing(v) for v in self['securities']['EQTY']]

    @property
    def etf(self) -> List[Response]:
        return [Response(v) for v in self['securities']['ETF']]
