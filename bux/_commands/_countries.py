from argparse import ArgumentParser
from .._user import UserAPI
from ._base import Command, register


@register
class Countries(Command):
    name = 'countries'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)

    def run(self) -> int:
        api = UserAPI(token=self.args.token)
        countries = api.securities().countries().requests()
        for country in countries:
            print(f'{country.name:16} {country.id}')
        return 0
