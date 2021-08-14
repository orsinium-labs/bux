from datetime import datetime
from decimal import Decimal
from typing import Any, Optional

from ._price import Price
from ._response import Response


class SecurityStats(Response):
    @property
    def dividend_frequency(self) -> str:
        """
        This is simply how often dividends are paid out.
        Sometimes it is quarterly, twice a year or annually.
        """
        return self['dividendFrequency']

    @property
    def dividend_per_share(self) -> Optional[Price]:
        """
        How much the company pays out in dividends, per share that you own.

        For example, if DPS is €0.50, you’ll get €0.50 for every share when
        dividends are paid out (keep in mind that dividends are subject to
        a withholding tax so the amount you receive may be lower).
        It’s calculated by dividing the total amount of dividends paid out
        divided by the number of outstanding shares.
        """
        if self['dividendPerShare'] is None:
            return None
        return Price(self['dividendPerShare'])

    @property
    def dividend_yield(self) -> Decimal:
        """
        This percentage figure shows how much a company pays out in dividends
        each year relative to its stock price.
        It’s calculated by dividing the dividend amount by the share price.
        """
        return Decimal(self['dividendYield'])

    @property
    def eps_ratio(self) -> Decimal:
        """
        This is one way to measure a firm’s profitability.
        EPS stands for ‘earnings per share.’
        It’s a ratio of the company’s total profit,
        divided by the total number of outstanding shares.
        """
        return Decimal(self['epsRatio'])

    @property
    def earnings_date(self) -> datetime:
        """
        The date of a company's next financial report (usually quarterly or annually).
        """
        return datetime.fromtimestamp(self['earningsDate'] / 1000)

    @property
    def ex_dividend_date(self) -> datetime:
        """
        This is the ‘cut off’ date for investors if they want to receive
        the company’s next dividend payout.

        If you want to be eligible for a company’s next dividend payout,
        you must be a shareholder before the ex-dividend date.
        If you purchase shares on or after the date,
        you won’t receive the upcoming payout.
        """
        return datetime.fromtimestamp(self['exDividendDate'] / 1000)

    @property
    def high_price_year(self) -> Price:
        """
        The highest price an asset has traded during the past 52 weeks.
        It’s based on the daily closing price.
        """
        return Price(self['highPrice52week'])

    @property
    def low_price_year(self) -> Price:
        """
        The lowest price an asset has traded during the past 52 weeks.
        It’s based on the daily closing price.
        """
        return Price(self['lowPrice52week'])

    @property
    def market_cap(self) -> Price:
        """
        Short for ‘market capitalisation,’ this is how much a company is worth.
        It’s calculated by multiplying the price of one share
        by the total number of outstanding shares.
        For example, a company with 20 million shares worth $100 each
        has a market cap of $2 billion.
        """
        return Price(self['marketCap'])

    @property
    def pe_ratio(self) -> Decimal:
        """
        P/E ratio is one way to figure out if a company is overvalued or undervalued.
        It compares the price of a company’s stock to how much profit it makes.
        P/E ratio is calculated by measuring the price of a share
        divided by its earnings per share (EPS).
        """
        return Decimal(self['peRatio'])

    @property
    def revenue(self) -> Any:
        """
        The total amount of money a company has generated
        by the sale of goods or services.
        Note, this is different to profit which is revenue minus expenses.
        """
        return self['revenue']

    @property
    def id(self) -> str:
        return self['securityId']
