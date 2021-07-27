from datetime import datetime

import bux


def test_me(api: bux.UserAPI):
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


def test_personal_data(api: bux.UserAPI):
    resp = api.personal_data().requests()
    fields = {'lastName', 'firstName', 'email'}
    assert set(resp) == fields
    assert '@' in resp.email


def test_portfolio(api: bux.UserAPI):
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


def test_following(api: bux.UserAPI):
    resp = api.following().requests()
    fields = {'securities'}
    assert set(resp) == fields
    assert resp.eqty[0].bid.amount >= 0


def test_security_graph(api: bux.UserAPI):
    resp = api.security('NL0011540547').graph().requests()
    fields = {'min', 'pricesTimeline', 'max'}
    assert set(resp) == fields
    assert resp.min >= 1
    assert resp.max >= 1
    assert resp.prices[0].price >= 1


def test_security_stats(api: bux.UserAPI):
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


def test_security_presentation(api: bux.UserAPI):
    resp = api.security('NL0011540547').presentation().requests()
    fields = {'marketHours', 'security', 'socialInfo', 'pendingOrders', 'forexQuote'}
    assert set(resp) == fields
    today = datetime.now().date()
    assert resp.market_hours.closing.date() == today
    assert resp.ticker_code == 'ABN'
