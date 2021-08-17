from argparse import ArgumentParser

import bux

from ._base import Command, register


@register
class Graph(Command):
    name = 'graph'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('--period', default='1d')
        parser.add_argument('--format', default='{time} {price:>8}')
        parser.add_argument('id')

    def run(self) -> int:
        api = bux.UserAPI(token=self.args.token)
        graph = api.security(self.args.id).graph(self.args.period).requests()
        for point in graph.prices:
            self.print(self.args.format.format(time=point.time, price=point.price))
        return 0
