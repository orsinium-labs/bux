from ._response import Response
from ._price import Price


class Security(Response):
    @property
    def _sec(self):
        return self

    @property
    def bid(self) -> Price:
        return Price(self._sec['bid'])

    @property
    def closing_bid(self) -> Price:
        return Price(self._sec['closingBid'])

    @property
    def opening_bid(self) -> Price:
        return Price(self._sec['openingBid'])

    @property
    def country_code(self) -> str:
        return self._sec['countryCode']

    @property
    def description(self) -> str:
        return self._sec['description']

    @property
    def id(self) -> str:
        return self._sec['id']

    @property
    def name(self) -> str:
        return self._sec['name']

    @property
    def security_type(self) -> str:
        return self._sec['securityType']

    @property
    def offer(self) -> Price:
        return Price(self._sec['offer'])

    @property
    def ticker_code(self) -> str:
        return self._sec['tickerCode']
