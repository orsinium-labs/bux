from typing import List

from ._response import Response
from ._security import SecurityNested


class Following(Response):
    @property
    def eqty(self) -> List[SecurityNested]:
        return [SecurityNested(v) for v in self['securities']['EQTY']]

    @property
    def etf(self) -> List[SecurityNested]:
        return [SecurityNested(v) for v in self['securities']['ETF']]
