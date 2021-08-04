from argparse import ArgumentParser
from .._user import UserAPI
from ._base import Command, register


@register
class Tag(Command):
    name = 'tag'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('tag')

    def run(self) -> int:
        api = UserAPI(token=self.args.token)
        matches = api.securities().filter_tag(self.args.tag).requests()
        for stock in matches.stocks:
            print(stock.id, stock.name)
        return 0
