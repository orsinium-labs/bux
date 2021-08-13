from argparse import ArgumentParser

import bux
from ._base import Command, register


@register
class Info(Command):
    name = 'info'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('id')

    def run(self) -> int:
        api = bux.UserAPI(token=self.args.token)
        info = api.security(self.args.id).presentation().requests()
        self.print(f'{info.security_type} [{info.ticker_code}] {info.name}')
        self.print(info.description)
        if info.key_information_url:
            self.print(info.key_information_url)
        self.print(' '.join(f'#{tag.id}' for tag in info.tags))
        self.print()

        self.print(f'bid: {info.bid.amount} {info.bid.currency}')
        self.print(f'ask: {info.offer.amount} {info.offer.currency}')
        self.print('graph types:', ', '.join(info.graph_types))
        return 0
