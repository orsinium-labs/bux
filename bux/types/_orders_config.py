from typing import List
from ._response import Response
from ._price import Price


class OrderType(Response):
    pass


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
