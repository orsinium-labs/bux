from ._price import Price
from ._security import Security


class ETF(Security):
    @property
    def today_low(self) -> Price:
        return Price(self['stats']['todayLow'])

    @property
    def today_high(self) -> Price:
        return Price(self['stats']['todayHigh'])
