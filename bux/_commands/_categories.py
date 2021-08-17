from argparse import ArgumentParser

import bux

from ._base import Command, register


@register
class Categories(Command):
    name = 'categories'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('--format', default='{id}')

    def run(self) -> int:
        api = bux.UserAPI(token=self.args.token)
        tags = api.securities().featured_tags().requests()
        for tag in tags:
            self.print(self.args.format.format(**tag))
        return 0
