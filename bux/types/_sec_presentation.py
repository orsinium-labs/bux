from typing import List
from ._market_hours import MarketHours
from ._tag import Tag
from ._security import Security


class SecurityPresentation(Security):
    @property
    def _sec(self):
        return self['security']

    @property
    def market_hours(self) -> MarketHours:
        return MarketHours(self['marketHours'])

    @property
    def exchange_id(self) -> str:
        return self['security']['exchangeId']

    @property
    def graph_types(self) -> List[str]:
        return self['security']['graphTypes']

    @property
    def status(self) -> str:
        return self['security']['status']

    @property
    def tags(self) -> List[Tag]:
        return [Tag(t) for t in self['security']['tags']]

    @property
    def following(self) -> int:
        return self['socialInfo']['following']

    @property
    def followers(self) -> int:
        return self['socialInfo']['followers']
