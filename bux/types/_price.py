from decimal import Decimal

from ._response import Response


class Price(Response):
    @property
    def amount(self) -> Decimal:
        return Decimal(self['amount'])

    @property
    def currency(self) -> str:
        return self['currency']

    @property
    def decimals(self) -> int:
        return self['decimals']

    def __str__(self) -> str:
        return f'{self.amount} {self.currency}'
