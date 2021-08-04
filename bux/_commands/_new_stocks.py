from argparse import ArgumentParser
from .._user import UserAPI
from ._base import Command, register


@register
class NewStocks(Command):
    name = 'new-stocks'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)

    def run(self) -> int:
        api = UserAPI(token=self.args.token)
        matches = api.securities().filter_new().requests()
        for stock in matches.stocks:
            print(stock.id, f'{stock.security_type:4}', stock.name)
        return 0
