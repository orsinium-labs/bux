import bux
from ._base import Command, register


@register
class Version(Command):
    name = 'version'

    def run(self) -> int:
        print(bux.__version__)
        return 0
