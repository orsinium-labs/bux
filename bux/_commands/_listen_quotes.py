from argparse import ArgumentParser
from .._ws import WebSocketAPI
from ._base import Command, register
from .. import types


@register
class ListenQuotes(Command):
    name = 'listen-quotes'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('--format', default='{id} {bid.amount:>8} {ask.amount:>8} {ask.currency}')
        parser.add_argument('id')

    async def run_async(self) -> int:
        async with WebSocketAPI(token=self.args.token) as api:
            async with api.quote(self.args.id):
                async for msg in api:
                    if isinstance(msg, types.WSQuote):
                        print(self.args.format.format(id=msg.id, bid=msg.bid, ask=msg.offer))
        return 0
