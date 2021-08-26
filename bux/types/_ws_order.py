from enum import Enum

from ._order import Order
from ._price import Price
from ._ws import WSResponse


class OrderState(Enum):
    CREATED = 'CREATED'
    EXECUTED = 'EXECUTED'
    PENDING = 'PENDING'
    CANCELLED = 'CANCELLED'
    CANCELLATION_REJECTED = 'CANCELLATION_REJECTED'
    CANCELLATION_PENDING = 'CANCELLATION_PENDING'
    EXPIRED = 'EXPIRED'
    REJECTED = 'REJECTED'


class WSOrder(Order, WSResponse):  # pragma: no cover
    @property
    def name(self) -> str:
        """Example: `S&P 500 Index ETF (Vanguard)`
        """
        return self['stockName']

    @property
    def number(self) -> int:
        return int(self['orderNumber'])

    @property
    def state(self) -> OrderState:
        return OrderState(self['orderState'])

    @property
    def price(self) -> Price:
        return Price(self['price'])

    @property
    def currency(self) -> str:
        return self['currency']

    @property
    def user_home_currency(self) -> str:
        return self['userHomeCurrency']
