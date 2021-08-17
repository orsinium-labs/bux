from typing import Optional

from ._price import Price
from ._response import Response


class Security(Response):
    @property
    def _sec(self) -> dict:
        return self

    @property
    def bid(self) -> Price:
        return Price(self._sec['bid'])

    @property
    def closing_bid(self) -> Price:
        return Price(self._sec['closingBid'])

    @property
    def country_code(self) -> Optional[str]:
        return self._sec.get('countryCode')

    @property
    def opening_bid(self) -> Optional[Price]:
        if not self._sec.get('openingBid'):
            return None
        return Price(self._sec['openingBid'])

    @property
    def description(self) -> Optional[str]:
        return self._sec.get('description')

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

    @property
    def today_low(self) -> Optional[Price]:
        if not self.get('stats'):
            return None
        return Price(self['stats']['todayLow'])

    @property
    def today_high(self) -> Optional[Price]:
        if not self.get('stats'):
            return None
        return Price(self['stats']['todayHigh'])


class SecurityNested(Security):
    """Like a regular security but with `following` and `followers` fields.

    For some reason, the API returns all regular security fields
    as nested into `security` if there is social info presented.
    We just unwrap it because "flat is better than nested".
    """
    @property
    def _sec(self):
        return self['security']

    @property
    def following(self) -> bool:
        return self['socialInfo']['following']

    @property
    def followers(self) -> int:
        return self['socialInfo']['followers']
