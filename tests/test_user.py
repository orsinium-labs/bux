from datetime import datetime
from decimal import Decimal

import bux


def check_has_all_getters(resp: bux.Response, exclude=(), unwrap=()):
    values = []
    for name, getter in vars(type(resp)).items():
        if name.startswith('_'):
            continue
        if not isinstance(getter, property):
            continue
        value = getattr(resp, name)
        if isinstance(value, bux.Response):
            value = dict(value)
        if isinstance(value, Decimal):
            value = str(value)
        if isinstance(value, datetime):
            value = value.timestamp() * 1000
        values.append(value)

    missed = []
    for name, value in resp.items():
        if name in exclude:
            continue
        if name in unwrap:
            continue
        if value not in values:
            missed.append(name)
    for group in unwrap:
        for name, value in resp[group].items():
            if name in exclude:
                continue
            if name in unwrap:
                continue
            if value not in values:
                missed.append(name)
    assert not missed


def test_me(api: bux.UserAPI, record_resp):
    resp = api.me().requests()
    fields = {
        'accountStatus',
        'usMarketDataSubscriptionActivated',
        'pinStatus',
        'communicationConfiguration',
        'profile',
        'etfAgreementAccepted',
        'accountType',
        'reassessmentInfo',
    }
    assert set(resp) == fields
    assert resp.account_status.isupper()
    assert resp.pin_status == 'ENABLED'
    assert '-' in resp.user_id
    check_has_all_getters(
        resp,
        exclude={'communicationConfiguration', 'reassessmentInfo', 'nickname'},
        unwrap={'profile'},
    )


def test_personal_data(api: bux.UserAPI, record_resp):
    resp = api.personal_data().requests()
    fields = {'lastName', 'firstName', 'email'}
    assert set(resp) == fields
    assert '@' in resp.email
    check_has_all_getters(resp)


def test_portfolio(api: bux.UserAPI, record_resp):
    resp = api.portfolio().requests()
    fields = {
        'accountValue',
        'allTimeDepositAndWithdraws',
        'allTimeTradesAmount',
        'availableCash',
        'cashBalance',
        'intraDayTradesAmount',
        'investedAmount',
        'marketsOpen',
        'orders',
        'positions',
        'previousClosingAmount',
        'reservedCash',
    }
    assert set(resp) == fields
    assert resp.account_value.amount >= 0
    check_has_all_getters(resp)


def test_following(api: bux.UserAPI, record_resp):
    resp = api.following().requests()
    fields = {'securities'}
    assert set(resp) == fields
    assert resp.eqty[0].bid.amount >= 0
    check_has_all_getters(
        resp.eqty[0],
        exclude={'stats'},
        unwrap={'security', 'socialInfo'},
    )


def test_security_graph(api: bux.UserAPI, record_resp):
    resp = api.security('NL0011540547').graph().requests()
    fields = {'min', 'pricesTimeline', 'max'}
    assert set(resp) == fields
    assert resp.min >= 1
    assert resp.max >= 1
    assert resp.prices[0].price >= 1
    check_has_all_getters(resp)
    check_has_all_getters(resp.prices[0])


def test_security_stats(api: bux.UserAPI, record_resp):
    resp = api.security('NL0011540547').stats().requests()
    fields = {
        'dividendFrequency',
        'dividendPerShare',
        'dividendYield',
        'earningsDate',
        'epsRatio',
        'exDividendDate',
        'highPrice52week',
        'lowPrice52week',
        'marketCap',
        'peRatio',
        'revenue',
        'securityId',
    }
    assert set(resp) == fields
    assert resp.market_cap.amount >= 10 ** 9
    assert resp.security_id == 'NL0011540547'
    check_has_all_getters(resp)


def test_security_presentation(api: bux.UserAPI, record_resp):
    resp = api.security('NL0011540547').presentation().requests()
    fields = {'marketHours', 'security', 'socialInfo', 'pendingOrders', 'forexQuote'}
    assert set(resp) == fields
    today = datetime.now().date()
    assert resp.market_hours.closing.date() == today
    assert resp.ticker_code == 'ABN'
    check_has_all_getters(
        resp,
        exclude={'pendingOrders', 'forexQuote', 'tags', 'stats'},
        unwrap={'security', 'socialInfo'},
    )
    check_has_all_getters(resp.market_hours)


def test_security_movers(api: bux.UserAPI, record_resp):
    resp = api.movers().requests()
    fields = {'losers', 'gainers', 'filters'}
    assert set(resp) == fields
    assert resp.gainers[0].ticker_code.isupper()
    check_has_all_getters(resp, exclude={'filters'})

    fields = {
        'bid',
        'closingBid',
        'countryCode',
        'description',
        'id',
        'name',
        'offer',
        'openingBid',
        'securityType',
        'stats',
        'tickerCode',
    }
    assert set(resp.gainers[0]) == fields
    check_has_all_getters(resp.gainers[0])
    check_has_all_getters(resp.losers[0])
    check_has_all_getters(resp.value_filters[0])
    check_has_all_getters(resp.toggle_filters[0])
