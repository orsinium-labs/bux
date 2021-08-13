from datetime import datetime

from ._response import Response


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
