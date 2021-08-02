from typing import List
from ._response import Response
from ._movers import SecurityMover
from ._tag import Tag


class TagMatches(Response):
    @property
    def parent_tag(self) -> Tag:
        return self['parentTag']

    @property
    def tags(self) -> List[Tag]:
        return [Tag(t) for t in self['tags']]

    @property
    def stocks(self) -> List[SecurityMover]:
        return [SecurityMover(s) for s in self['stocks']]
