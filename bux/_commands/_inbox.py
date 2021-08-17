from argparse import ArgumentParser

import bux

from ._base import Command, register


@register
class Inbox(Command):
    name = 'inbox'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)

    def run(self) -> int:
        api = bux.UserAPI(token=self.args.token)
        messages = api.inbox().requests()
        for msg in messages:
            self.print(f'{msg.time.date()} {msg.title}')
            self.print(' ', msg.description)
            if msg.link:
                self.print(' ', msg.link)
        return 0
