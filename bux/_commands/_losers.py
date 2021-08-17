from argparse import ArgumentParser

import bux

from ._base import Command, register


@register
class Losers(Command):
    name = 'losers'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)

    def run(self) -> int:
        api = bux.UserAPI(token=self.args.token)
        movers = api.securities().movers().requests()
        for stock in movers.losers:
            gain = (stock.bid.amount / stock.closing_bid.amount - 1) * 100
            self.print(f'{stock.id} {stock.name:25} {gain:+.02f}%')
        return 0
