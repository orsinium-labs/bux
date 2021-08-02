from typing import List
from ._response import Response
from ._market_hours import MarketHours
from ._price import Price
from ._tag import Tag


class SecurityPresentation(Response):
    @property
    def market_hours(self) -> MarketHours:
        return MarketHours(self['marketHours'])

    @property
    def bid(self) -> Price:
        return Price(self['security']['bid'])

    @property
    def closing_bid(self) -> Price:
        return Price(self['security']['closingBid'])

    @property
    def country_code(self) -> str:
        return self['security']['countryCode']

    @property
    def description(self) -> str:
        return self['security']['description']

    @property
    def exchange_id(self) -> str:
        return self['security']['exchangeId']

    @property
    def graph_types(self) -> List[str]:
        return self['security']['graphTypes']

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
    def status(self) -> str:
        return self['security']['status']

    @property
    def offer(self) -> Price:
        return Price(self['security']['offer'])

    # TODO: check if this field exists
    @property
    def opening_bid(self) -> Price:
        return Price(self['security']['openingBid'])

    @property
    def tags(self) -> List[Tag]:
        return [Tag(t) for t in self['security']['tags']]

    @property
    def ticker_code(self) -> str:
        return self['security']['tickerCode']

    @property
    def following(self) -> int:
        return self['socialInfo']['following']

    @property
    def followers(self) -> int:
        return self['socialInfo']['followers']
