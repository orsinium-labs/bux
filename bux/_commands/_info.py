from argparse import ArgumentParser
from textwrap import wrap

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
        self.print(f'{info.security_type} [{info.ticker_code}] {info.name}\n')
        if info.description is not None:
            self.print(*wrap(info.description, width=80), sep='\n', end='\n\n')
        self.print(' '.join(f'#{tag.id}' for tag in info.tags), end='\n\n')

        self.print_table({
            'bid':          info.bid,
            'opening bid':  info.opening_bid,
            'closing bid':  info.closing_bid,
            'ask':          info.offer,
            'graph types':  ', '.join(info.graph_types),
            'today low':    info.today_low,
            'today high':   info.today_high,
            'country':      info.country_code,
            'exchange':     info.exchange_id,
            'status':       info.status,
            'following?':   info.following,
            'more':         info.key_information_url,
        })
        return 0
