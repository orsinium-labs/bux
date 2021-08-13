from argparse import ArgumentParser

from .._user import UserAPI
from ._base import Command, register


@register
class Countries(Command):
    name = 'countries'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('--format', default='{name:16} {id}')

    def run(self) -> int:
        api = UserAPI(token=self.args.token)
        countries = api.securities().countries().requests()
        for country in countries:
            print(self.args.format.format(**country))
        return 0
