from argparse import ArgumentParser

import bux

from ._base import Command, register


@register
class Tag(Command):
    name = 'tag'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('--format', default='{id} [{tickerCode}] {name}')
        parser.add_argument('tag')

    def run(self) -> int:
        api = bux.UserAPI(token=self.args.token)
        matches = api.securities().filter_tag(self.args.tag).requests()
        for stock in matches.stocks:
            self.print(self.args.format.format(**stock))
        return 0
