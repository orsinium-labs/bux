from argparse import ArgumentParser

import bux

from ._base import Command, register


@register
class Portfolio(Command):
    name = 'portfolio'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)

    def run(self) -> int:
        api = bux.UserAPI(token=self.args.token)
        portfolio = api.portfolio().requests()
        self.print_table({
            'cash balance':     portfolio.cash_balance,
            'available cash':   portfolio.available_cash,
            'account value':    portfolio.account_value,
            'invested amount':  portfolio.invested_amount,
            'all time trades':  portfolio.all_time_trades_amount,
        })
        self.print()
        if portfolio.orders:
            self.print('Pending orders:')
            for order in portfolio.orders:
                self.print(f'  {order.quantity} stocks of "{order.name}"', end=' ')
                self.print(f'{order.security_type} ({order.security_id})')
        if portfolio.positions:
            self.print('Positions:')
            for pos in portfolio.positions:
                self.print(f'  {pos.quantity} x {pos.average_purchase_price:7} | ', end=' ')
                self.print(f'"{pos.name}" {pos.type} ({pos.id})')
        return 0
