from argparse import ArgumentParser
from datetime import date

import bux

from ._base import Command, register


@register
class Dividends(Command):
    name = 'dividends'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('--format', default='{date}: {id} {securityType} [{tickerCode}] {name}')

    def run(self) -> int:
        api = bux.UserAPI(token=self.args.token)
        matches = api.securities().filter_dividends().requests()

        today = date.today()
        for stock in matches.stocks:
            stat = api.security(stock.id).stats().requests()
            div_date = stat.ex_dividend_date.date()
            if div_date < today:
                continue
            self.print(self.args.format.format(**stock, **stat, date=div_date))
        return 0
