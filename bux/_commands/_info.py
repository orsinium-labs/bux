from argparse import ArgumentParser
from .._user import UserAPI
from ._base import Command, register


@register
class Info(Command):
    name = 'info'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('id')

    def run(self) -> int:
        api = UserAPI(token=self.args.token)
        info = api.security(self.args.id).presentation().requests()
        print(f'{info.security_type} [{info.ticker_code}] {info.name}')
        print(info.description)
        if info.key_information_url:
            print(info.key_information_url)
        print(' '.join(f'#{tag.id}' for tag in info.tags))
        print()

        print('bid', info.bid.amount, info.bid.currency)
        print('ask', info.offer.amount, info.offer.currency)
        print('graph types:', ','.join(info.graph_types))
        return 0
