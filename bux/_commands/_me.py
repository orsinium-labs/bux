from argparse import ArgumentParser
from .._user import UserAPI
from ._base import Command, register


@register
class Me(Command):
    name = 'me'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)

    def run(self) -> int:
        api = UserAPI(token=self.args.token)
        resp = api.personal_data().requests()
        print(f'{resp.first_name} {resp.last_name} <{resp.email}>')
        return 0
