from argparse import ArgumentParser

import bux

from ._base import Command, register


@register
class Countries(Command):
    name = 'countries'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('--format', default='{name:16} {id}')

    def run(self) -> int:
        api = bux.UserAPI(token=self.args.token)
        countries = api.securities().countries().requests()
        for country in countries:
            self.print(self.args.format.format(**country))
        return 0
