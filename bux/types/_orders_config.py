from datetime import datetime
from typing import List, Optional

from ._price import Price
from ._response import Response


class TradingType(Response):
    @property
    def name(self) -> str:
        return self['tradingType']

    @property
    def fee(self) -> Price:
        return Price(self['fee'])


class ExecutionWindow(Response):
    @property
    def start(self) -> datetime:
        return datetime.fromtimestamp(self['windowStart'] / 1000)

    @property
    def end(self) -> datetime:
        return datetime.fromtimestamp(self['windowEnd'] / 1000)


class OrderType(Response):
    @property
    def name(self) -> str:
        return self['displayedType']

    @property
    def expiration_date(self) -> Optional[datetime]:
        if 'expirationDate' not in self:
            return None
        return datetime.fromtimestamp(self['expirationDate'] / 1000)

    @property
    def execution_windows(self) -> List[ExecutionWindow]:
        return [ExecutionWindow(w) for w in self['executionWindows']]

    @property
    def trading_types(self) -> List[TradingType]:
        return [TradingType(w) for w in self['tradingTypes']]

    @property
    def fee(self) -> Price:
        assert len(self.trading_types) == 1
        return self.trading_types[0].fee


class OrdersConfig(Response):
    @property
    def available_cash(self) -> Price:
        return Price(self['availableCash'])

    @property
    def available_quantity(self) -> int:
        return int(self['availableQuantity'])

    @property
    def bid(self) -> Price:
        return Price(self['bid'])

    @property
    def offer(self) -> Price:
        return Price(self['offer'])

    @property
    def order_types(self) -> List[OrderType]:
        return [OrderType(t) for t in self['clientOrderTypes']]

    @property
    def tax_rate(self) -> int:
        return int(self['taxRate'])

    @property
    def value_limit(self) -> Price:
        return Price(self['valueLimit'])

    @property
    def share_limit(self) -> int:
        return int(self['shareLimit'])
