from typing import List
from ._response import Response
from ._security import Security


class SecurityFollowing(Security):
    @property
    def _sec(self):
        return self['security']

    @property
    def following(self) -> bool:
        return self['socialInfo']['following']

    @property
    def followers(self) -> int:
        return self['socialInfo']['followers']


class Following(Response):
    @property
    def eqty(self) -> List[SecurityFollowing]:
        return [SecurityFollowing(v) for v in self['securities']['EQTY']]

    @property
    def etf(self) -> List[Response]:
        return [Response(v) for v in self['securities']['ETF']]
