from ._price import Price
from ._response import Response


class WSResponse(Response):
    pass


class WSQuote(WSResponse):  # pragma: no cover
    @property
    def id(self) -> str:
        return self['id']

    @property
    def bid(self) -> Price:
        return Price(self['bid'])

    @property
    def offer(self) -> Price:
        return Price(self['offer'])
