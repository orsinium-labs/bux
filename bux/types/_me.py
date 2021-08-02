from ._response import Response


class Me(Response):
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

    @property
    def us_market_data_subscription_activated(self) -> bool:
        return self['usMarketDataSubscriptionActivated']
