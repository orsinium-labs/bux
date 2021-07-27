from ._base import register, Command
from .._guest import GuestAPI


@register
class GetToken(Command):
    name = 'get-token'

    def run(self) -> int:
        email = input('1. Enter email: ')
        api = GuestAPI()
        api.request_link(email).requests()
        print('2. Check your mailbox.')
        magic_link = input('3. Enter magic link: ')
        token = api.get_token(magic_link).requests()
        print('Your token:', token)
        return 0
