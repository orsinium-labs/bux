from argparse import ArgumentParser

import bux

from ._base import Command, register


@register
class ETFs(Command):
    name = 'etfs'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('--format', default='{id} [{tickerCode:4}] {name}')

    def run(self) -> int:
        api = bux.UserAPI(token=self.args.token)
        etfs = api.securities().etfs().requests()
        for etf in etfs:
            self.print(self.args.format.format(**etf))
        return 0
