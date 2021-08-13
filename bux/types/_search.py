from typing import List

from ._response import Response
from ._security import SecurityNested
from ._tag import Tag


class Search(Response):

    @property
    def eqty(self) -> List[SecurityNested]:
        return [SecurityNested(p) for p in self['securities']['EQTY']]

    @property
    def etf(self) -> List[SecurityNested]:
        return [SecurityNested(p) for p in self['securities']['ETF']]

    @property
    def eqty_under_price(self) -> List[SecurityNested]:
        return [SecurityNested(p) for p in self['securitiesUnderPrice']['EQTY']]

    @property
    def etf_under_price(self) -> List[SecurityNested]:
        return [SecurityNested(p) for p in self['securitiesUnderPrice']['ETF']]

    @property
    def tags(self) -> List[Tag]:
        return [Tag(p) for p in self['tags']]
