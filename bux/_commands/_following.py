from argparse import ArgumentParser

from .._user import UserAPI
from ._base import Command, register


@register
class Following(Command):
    name = 'following'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)

    def run(self) -> int:
        api = UserAPI(token=self.args.token)
        following = api.following().requests()
        groups = (following.eqty, following.etf)
        for group in groups:
            for sec in group:
                gain = (sec.bid.amount / sec.closing_bid.amount - 1) * 100
                gain_abs = sec.bid.amount - sec.closing_bid.amount
                print(f'{sec.id} {sec.name:25} ', end='')
                print(f'{gain:+.02f}% ({gain_abs:+.02f} {sec.bid.currency}) ', end='')
                print(f'={sec.bid.amount} {sec.bid.currency}')
        return 0
