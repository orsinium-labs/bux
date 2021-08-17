from typing import Any, Dict

from ._price import Price
from ._response import Response


class Position(Response):
    @property
    def _pos(self) -> Dict[str, Any]:
        return self

    @property
    def buy_amount(self) -> Price:
        return Price(self._pos['allTimeChanges']['buyAmount'])

    @property
    def cash_change(self) -> Price:
        return Price(self._pos['allTimeChanges']['cashChange'])

    @property
    def sell_amount(self) -> Price:
        return Price(self._pos['allTimeChanges']['sellAmount'])

    @property
    def average_purchase_price(self) -> Price:
        return Price(self._pos['averagePurchasePrice'])

    @property
    def average_purchase_price_in_user_currency(self) -> Price:
        return Price(self._pos['averagePurchasePriceInUserCurrency'])

    @property
    def investment_amount(self) -> Price:
        return Price(self._pos['investmentAmount'])

    @property
    def previous_closing_amount(self) -> Price:
        return Price(self._pos['previousClosingAmount'])

    @property
    def quantity(self) -> int:
        return int(self._pos['quantity'])

    @property
    def today_quantity(self) -> int:
        return int(self._pos['todayPerformance']['quantity'])

    @property
    def change_amount(self) -> Price:
        return Price(self._pos['todayPerformance']['changeAmount'])

    @property
    def intra_day_trades_amount(self) -> Price:
        return Price(self._pos['todayPerformance']['intraDayTradesAmount'])
