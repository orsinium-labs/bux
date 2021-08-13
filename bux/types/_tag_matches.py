from typing import List

from ._movers import Security
from ._response import Response
from ._tag import Tag


class TagMatches(Response):
    @property
    def parent_tag(self) -> Tag:
        return self['parentTag']

    @property
    def tags(self) -> List[Tag]:
        return [Tag(t) for t in self['tags']]

    @property
    def stocks(self) -> List[Security]:
        return [Security(s) for s in self['stocks']]
