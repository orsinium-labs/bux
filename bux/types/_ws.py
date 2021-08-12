from ._response import Response
from ._price import Price


class WSQuote(Response):
    @property
    def id(self) -> str:
        return self['id']

    @property
    def bid(self) -> Price:
        return Price(self['bid'])

    @property
    def offer(self) -> Price:
        return Price(self['offer'])
