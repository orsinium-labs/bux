from datetime import datetime
from decimal import Decimal
from typing import List

from ._response import Response


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
