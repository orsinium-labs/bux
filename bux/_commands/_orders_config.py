from argparse import ArgumentParser

import bux

from ._base import Command, register


@register
class OrdersConfig(Command):
    name = 'orders-config'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('id')

    def run(self) -> int:
        api = bux.UserAPI(token=self.args.token)
        conf = api.security(self.args.id).orders_config().requests()
        self.print_table({
            'available cash': conf.available_cash,
            'available quantity': conf.available_quantity,
            'bid':          conf.bid,
            'offer':        conf.offer,
            'tax rate':     conf.tax_rate,
            'value limit':  conf.value_limit,
            'share limit':  conf.share_limit,
        })

        for otype in conf.order_types:
            self.print(f'\n{otype.name}:')
            if otype.expiration_date:
                self.print(f'expires {otype.expiration_date}')
            self.print(f'fee {otype.fee}')
            print('execution windows:')
            for win in otype.execution_windows:
                self.print(f'  {win.start} - {win.end}')
        return 0
