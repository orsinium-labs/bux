from argparse import ArgumentParser

import bux

from ._base import Command, register


@register
class Order(Command):
    name = 'order'

    @staticmethod
    def init_parser(parser: ArgumentParser) -> None:
        parser.add_argument('--token', required=True)
        parser.add_argument('--pin', required=True)
        parser.add_argument(
            '-q', '--quantity', default=1, type=int,
            help='how many stocks to trade',
        )
        parser.add_argument('-t', '--type', default='BASIC')
        parser.add_argument('--dry', action='store_true')
        parser.add_argument('direction', choices=('buy', 'sell'))
        parser.add_argument('id')

    def run(self) -> int:
        api = bux.UserAPI(token=self.args.token)

        stock = api.security(self.args.id).presentation().requests()
        print(stock.name)

        conf = api.security(self.args.id).orders_config().requests()
        q: int = self.args.quantity
        assert q != 0
        direction: str = self.args.direction
        price = conf.offer if direction == 'buy' else conf.bid
        s = '' if q == 1 else 's'
        print(f'You will {direction} {abs(q)} stock{s} for ~{price}')

        for otype in conf.order_types:
            if otype.name == self.args.type:
                break
        else:
            print(f'Unknown order type: {self.args.type}')
            return 1
        print(f'\nOrder type is {otype.name}:')
        print(f'  fee {otype.fee}')
        if otype.expiration_date:
            self.print(f'  expires {otype.expiration_date}')
        print('  execution windows:')
        for win in otype.execution_windows:
            self.print(f'    {win.start} - {win.end}')

        access_token = api.authorize(pin=self.args.pin).requests()
        if self.args.dry:
            return 0
        return self._execute(fee=otype.fee, access_token=access_token)

    def _execute(
        self,
        fee: bux.types.Price,
        access_token: str,
    ) -> int:  # pragma: no-cover
        yes = input('type YES to proceed: ')
        if yes != 'YES':
            return 1
        api = bux.UserAPI(token=self.args.token)
        order = api.security(self.args.id).order(
            direction=self.args.direction.upper(),
            quantity=self.args.quantity,
            type=self.args.type,
            fee=fee,
            access_token=access_token,
        ).requests()
        print('ORDER IS EXECUTED')
        print(order.id)
        return 0
