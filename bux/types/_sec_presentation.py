from typing import List, Optional
from ._market_hours import MarketHours
from ._tag import Tag
from ._security import Security


class SecurityPresentation(Security):
    @property
    def _sec(self) -> dict:
        return self['security']

    @property
    def market_hours(self) -> MarketHours:
        return MarketHours(self['marketHours'])

    @property
    def exchange_id(self) -> str:
        return self._sec['exchangeId']

    @property
    def graph_types(self) -> List[str]:
        return self._sec['graphTypes']

    @property
    def status(self) -> str:
        return self._sec['status']

    @property
    def tags(self) -> List[Tag]:
        return [Tag(t) for t in self._sec['tags']]

    @property
    def key_information_url(self) -> Optional[str]:
        return self._sec.get('keyInformationURL')

    @property
    def following(self) -> int:
        return self['socialInfo']['following']

    @property
    def followers(self) -> int:
        return self['socialInfo']['followers']
