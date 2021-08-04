from argparse import ArgumentParser
from .._user import UserAPI
from ._base import Command, register


@register
class Categories(Command):
    name = 'categories'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)

    def run(self) -> int:
        api = UserAPI(token=self.args.token)
        tags = api.securities().featured_tags().requests()
        for tag in tags:
            print(tag.id)
        return 0
