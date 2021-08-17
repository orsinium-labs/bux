from argparse import ArgumentParser

import bux

from ._base import Command, register


@register
class Tags(Command):
    name = 'tags'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('--format', default='{id}')
        parser.add_argument('category')

    def run(self) -> int:
        api = bux.UserAPI(token=self.args.token)
        matches = api.securities().filter_tag(self.args.category).requests()
        for tag in matches.tags:
            self.print(self.args.format.format(**tag))
        return 0
