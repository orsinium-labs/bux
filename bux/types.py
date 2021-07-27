from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, List


class Response(Dict[str, Any]):
    def __repr__(self) -> str:
        r = super().__repr__()
        return f'{type(self).__name__}({r})'


class Me(Response):
    @property
    def account_status(self) -> str:
        return self['accountStatus']

    @property
    def account_type(self) -> str:
        return self['accountType']

    @property
    def pin_status(self) -> str:
        return self['pinStatus']

    @property
    def username(self) -> str:
        return self['profile']['nickname'] or ''

    @property
    def user_id(self) -> str:
        return self['profile']['userId']


class PersonalData(Response):
    @property
    def email(self) -> str:
        return self['email']

    @property
    def first_name(self) -> str:
        return self['firstName']

    @property
    def last_name(self) -> str:
        return self['lastName']


class Price(Response):
    @property
    def amount(self) -> Decimal:
        return Decimal(self['amount'])

    @property
    def currency(self) -> str:
        return self['currency']

    @property
    def decimals(self) -> int:
        return self['decimals']


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
    def positions(self) -> Response:
        return Response(self['positions'])


class SecurityFollowing(Response):
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


class Following(Response):
    @property
    def eqty(self) -> List[SecurityFollowing]:
        return [SecurityFollowing(v) for v in self['securities']['EQTY']]

    @property
    def etf(self) -> List[Response]:
        return [Response(v) for v in self['securities']['ETF']]


class MarketHours(Response):
    @property
    def closing(self) -> datetime:
        return datetime.fromtimestamp(self['closingTime'] / 1000)

    @property
    def opening(self) -> datetime:
        return datetime.fromtimestamp(self['openingTime'] / 1000)

    @property
    def is_open(self) -> bool:
        return self['isOpen']


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

    @property
    def tags(self) -> List[str]:
        return [t['id'] for t in self['security']['tags']]

    @property
    def ticker_code(self) -> str:
        return self['security']['tickerCode']


class SecurityStats(Response):
    @property
    def dividend_frequency(self) -> str:
        return self['dividendFrequency']

    @property
    def dividend_per_share(self) -> Price:
        return Price(self['dividendPerShare'])

    @property
    def dividend_yield(self) -> Decimal:
        return Decimal(self['dividendYield'])

    @property
    def eps_ratio(self) -> Decimal:
        return Decimal(self['epsRatio'])

    @property
    def earnings_date(self) -> date:
        return datetime.fromtimestamp(self['earningsDate'] / 1000).date()

    @property
    def ex_dividend_date(self) -> date:
        return datetime.fromtimestamp(self['exDividendDate'] / 1000).date()

    @property
    def high_price_year(self) -> Price:
        return Price(self['highPrice52week'])

    @property
    def low_price_year(self) -> Price:
        return Price(self['lowPrice52week'])

    @property
    def market_cap(self) -> Price:
        return Price(self['marketCap'])

    @property
    def pe_ratio(self) -> Decimal:
        return Decimal(self['peRatio'])

    @property
    def revenue(self) -> Any:
        return self['revenue']

    @property
    def security_id(self) -> str:
        return self['securityId']


class PricePoint(Response):
    @property
    def price(self) -> Decimal:
        return Decimal(self['price'])

    @property
    def time(self) -> datetime:
        return datetime.fromtimestamp(self['time'] / 1000)


class SecurityGraph(Response):
    @property
    def max(self) -> Decimal:
        return Decimal(self['max'])

    @property
    def min(self) -> Decimal:
        return Decimal(self['min'])

    @property
    def prices(self) -> List[PricePoint]:
        return [PricePoint(p) for p in self['pricesTimeline']]
