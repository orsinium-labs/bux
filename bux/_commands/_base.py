import asyncio
from argparse import ArgumentParser
from typing import Any, Dict, TextIO, Type, TypeVar


commands: Dict[str, Type['Command']] = dict()
T = TypeVar('T', bound=Type['Command'])


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
        return asyncio.run(self.run_async())    # pragma: no cover

    async def run_async(self) -> int:
        raise NotImplementedError    # pragma: no cover

    def print(self, *args: str, end='\n', sep=' ') -> None:
        print(*args, file=self.stream, end=end, sep=sep)

    def print_table(self, table: Dict[str, Any]) -> None:
        width = max(len(key) for key in table) + 1
        for field, value in table.items():
            if value is None:
                continue
            self.print(f'{field.ljust(width)} {value}')
