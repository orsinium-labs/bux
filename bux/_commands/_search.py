from argparse import ArgumentParser
from .._user import UserAPI
from ._base import Command, register


@register
class Search(Command):
    name = 'search'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('query')

    def run(self) -> int:
        api = UserAPI(token=self.args.token)
        matches = api.search(self.args.query).requests()
        groups = {
            'Equities': matches.eqty,
            'Equities under price': matches.eqty_under_price,
            'ETFs': matches.etf,
            'ETFs under price': matches.etf_under_price,
        }
        for group_name, group in groups.items():
            if group:
                print(f'{group_name}:')
            for stock in group:
                print(' ', stock.id, stock.name)
        return 0