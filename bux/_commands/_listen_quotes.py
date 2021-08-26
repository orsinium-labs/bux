from argparse import ArgumentParser

import bux

from ._base import Command, register


@register
class ListenQuotes(Command):
    name = 'listen-quotes'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('--format', default='{id} {bid.amount:>8} {ask.amount:>8} {ask.currency}')
        parser.add_argument('ids', nargs='+')

    async def run_async(self) -> int:  # pragma: no cover
        async with bux.WebSocketAPI(token=self.args.token) as api:
            topics = [api.topics.security(id) for id in self.args.ids]
            async with api.listen(*topics):
                async for msg in api:
                    if isinstance(msg, bux.types.WSQuote):
                        self.print(self.args.format.format(id=msg.id, bid=msg.bid, ask=msg.offer))
        return 0
