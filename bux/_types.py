from decimal import Decimal


class Me(dict):
    @property
    def account_status(self) -> str:
        return self['accountStatus']

    @property
    def account_type(self) -> str:
        return self['accountType']

    @property
    def pin_status(self) -> str:
        return self['pinStatus']

    @property
    def username(self) -> str:
        return self['profile']['nickname'] or ''

    @property
    def user_id(self) -> str:
        return self['profile']['userId']


class PersonalData(dict):
    @property
    def email(self) -> str:
        return self['email']

    @property
    def first_name(self) -> str:
        return self['firstName']

    @property
    def last_name(self) -> str:
        return self['lastName']


class Price(dict):
    @property
    def amount(self) -> Decimal:
        return Decimal(self['amount'])

    @property
    def currency(self) -> str:
        return self['currency']

    @property
    def decimals(self) -> int:
        return self['decimals']


class Portfolio(dict):
    @property
    def account_value(self) -> Price:
        return Price(self['accountValue'])

    ...


class Following(dict):
    ...
