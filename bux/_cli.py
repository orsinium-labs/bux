import sys
from argparse import ArgumentParser
from typing import List, NoReturn, TextIO

from ._commands import commands


def main(argv: List[str], stream: TextIO) -> int:
    parser = ArgumentParser('python3 -m bux')
    subparsers = parser.add_subparsers()
    parser.set_defaults(cmd=None)

    for name, cmd_class in commands.items():
        subparser = subparsers.add_parser(name=name)
        subparser.set_defaults(cmd=cmd_class)
        cmd_class.init_parser(subparser)
    args = parser.parse_args(argv)

    cmd_class = args.cmd
    if cmd_class is None:    # pragma: no cover
        parser.print_help()
        return 1
    cmd = cmd_class(args=args, stream=stream)
    return cmd.run()


def entrypoint() -> NoReturn:
    sys.exit(main(argv=sys.argv[1:], stream=sys.stdout))
