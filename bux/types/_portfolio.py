from typing import Any, Dict, List, Optional

from ._position import Position
from ._price import Price
from ._response import Response


class PortfolioPosition(Position):
    @property
    def _pos(self) -> Dict[str, Any]:
        return self['position']

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

    @property
    def closing_bid(self) -> Optional[Price]:
        if 'closingBid' not in self['security']:
            return None
        return Price(self['security']['closingBid'])

    @property
    def bid(self) -> Optional[Price]:
        if 'bid' not in self['security']:
            return None
        return Price(self['security']['bid'])


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
    def positions_eqty(self) -> List[PortfolioPosition]:
        return [PortfolioPosition(p) for p in self['positions']['EQTY']]

    @property
    def positions_etf(self) -> List[PortfolioPosition]:
        return [PortfolioPosition(p) for p in self['positions']['ETF']]
