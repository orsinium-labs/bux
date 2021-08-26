import bux

from ._base import Command, register


@register
class GetToken(Command):
    name = 'get-token'

    def run(self) -> int:  # pragma: no cover
        email = input('1. Enter email: ')
        api = bux.GuestAPI()
        api.request_link(email).requests()
        self.print('2. Check your mailbox.')
        magic_link = input('3. Enter magic link: ')
        token = api.get_token(magic_link).requests()
        self.print('Your token:', token)
        return 0
