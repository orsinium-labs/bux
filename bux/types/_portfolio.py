from typing import List, Optional

from ._price import Price
from ._response import Response


class Position(Response):
    @property
    def buy_amount(self) -> Price:
        return Price(self['position']['allTimeChanges']['buyAmount'])

    @property
    def cash_change(self) -> Price:
        return Price(self['position']['allTimeChanges']['cashChange'])

    @property
    def sell_amount(self) -> Price:
        return Price(self['position']['allTimeChanges']['sellAmount'])

    @property
    def average_purchase_price(self) -> Price:
        return Price(self['position']['averagePurchasePrice'])

    @property
    def average_purchase_price_in_user_currency(self) -> Price:
        return Price(self['position']['averagePurchasePriceInUserCurrency'])

    @property
    def investment_amount(self) -> Price:
        return Price(self['position']['investmentAmount'])

    @property
    def previous_closing_amount(self) -> Price:
        return Price(self['position']['previousClosingAmount'])

    @property
    def quantity(self) -> int:
        return int(self['position']['quantity'])

    @property
    def today_quantity(self) -> int:
        return int(self['position']['todayPerformance']['quantity'])

    @property
    def change_amount(self) -> Price:
        return Price(self['position']['todayPerformance']['changeAmount'])

    @property
    def intra_day_trades_amount(self) -> Price:
        return Price(self['position']['todayPerformance']['intraDayTradesAmount'])

    @property
    def id(self) -> str:
        return self['security']['id']

    @property
    def name(self) -> str:
        return self['security']['name']

    @property
    def country_code(self) -> Optional[str]:
        return self['security'].get('countryCode')

    @property
    def offer(self) -> Price:
        return Price(self['security']['offer'])


class Portfolio(Response):
    @property
    def account_value(self) -> Price:
        return Price(self['accountValue'])

    @property
    def all_time_deposit_and_withdraws(self) -> Price:
        return Price(self['allTimeDepositAndWithdraws'])

    @property
    def all_time_trades_amount(self) -> Price:
        return Price(self['allTimeTradesAmount'])

    @property
    def available_cash(self) -> Price:
        return Price(self['availableCash'])

    @property
    def cash_balance(self) -> Price:
        return Price(self['cashBalance'])

    @property
    def intra_day_trades_amount(self) -> Price:
        return Price(self['intraDayTradesAmount'])

    @property
    def invested_amount(self) -> Price:
        return Price(self['investedAmount'])

    @property
    def previous_closing_amount(self) -> Price:
        return Price(self['previousClosingAmount'])

    @property
    def reserved_cash(self) -> Price:
        return Price(self['reservedCash'])

    @property
    def markets_open(self) -> bool:
        return self['marketsOpen']

    @property
    def orders(self) -> Response:
        return Response(self['orders'])

    @property
    def positions_eqty(self) -> List[Position]:
        return [Position(p) for p in self['positions']['EQTY']]

    @property
    def positions_etf(self) -> List[Position]:
        return [Position(p) for p in self['positions']['ETF']]
