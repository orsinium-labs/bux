from datetime import datetime
from decimal import Decimal
from typing import Any, Optional

from ._price import Price
from ._response import Response


class SecurityStats(Response):
    @property
    def dividend_frequency(self) -> str:
        return self['dividendFrequency']

    @property
    def dividend_per_share(self) -> Optional[Price]:
        if self['dividendPerShare'] is None:
            return None
        return Price(self['dividendPerShare'])

    @property
    def dividend_yield(self) -> Decimal:
        return Decimal(self['dividendYield'])

    @property
    def eps_ratio(self) -> Decimal:
        return Decimal(self['epsRatio'])

    @property
    def earnings_date(self) -> datetime:
        return datetime.fromtimestamp(self['earningsDate'] / 1000)

    @property
    def ex_dividend_date(self) -> datetime:
        return datetime.fromtimestamp(self['exDividendDate'] / 1000)

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
