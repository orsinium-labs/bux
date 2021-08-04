from argparse import ArgumentParser
from .._user import UserAPI
from ._base import Command, register


@register
class Gainers(Command):
    name = 'gainers'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)

    def run(self) -> int:
        api = UserAPI(token=self.args.token)
        movers = api.securities().movers().requests()
        for stock in movers.gainers:
            gain = (stock.bid.amount / stock.closing_bid.amount - 1) * 100
            print(f'{stock.id} {stock.name:25} {gain:+.02f}%')
        return 0
