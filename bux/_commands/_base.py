from argparse import ArgumentParser
from typing import Any, Dict, TextIO, Type, TypeVar


commands: Dict[str, Type["Command"]] = dict()
T = TypeVar("T", bound=Type["Command"])


def register(cmd: T) -> T:
    """Decorator to register a command in CLI.
    """
    commands[cmd.name] = cmd
    return cmd


class Command:
    name: str

    def __init__(self, args: Any, stream: TextIO) -> None:
        self.args = args
        self.stream = stream

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        return

    def run(self) -> int:
        raise NotImplementedError
