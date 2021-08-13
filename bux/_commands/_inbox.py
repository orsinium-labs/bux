from argparse import ArgumentParser

from .._user import UserAPI
from ._base import Command, register


@register
class Inbox(Command):
    name = 'inbox'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)

    def run(self) -> int:
        api = UserAPI(token=self.args.token)
        messages = api.inbox().requests()
        for msg in messages:
            print(f'{msg.time.date()} {msg.title}')
            print(' ', msg.description)
            if msg.link:
                print(' ', msg.link)
        return 0
