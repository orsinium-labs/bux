from datetime import datetime

import bux

from .helpers import check_has_all_getters, check_has_fields


def test_security_graph(api: bux.UserAPI, record_resp):
    resp = api.security('NL0011540547').graph().requests()
    check_has_fields(resp, {'min', 'pricesTimeline', 'max'})
    assert resp.min >= 1
    assert resp.max >= 1
    assert resp.prices[0].price >= 1
    check_has_all_getters(resp)
    check_has_all_getters(resp.prices[0])


def test_security_stats(api: bux.UserAPI, record_resp):
    resp = api.security('NL0011540547').stats().requests()
    check_has_fields(
        resp,
        must={
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
        },
    )
    assert resp.market_cap.amount >= 10 ** 9
    assert resp.id == 'NL0011540547'
    check_has_all_getters(resp)


def test_security_presentation(api: bux.UserAPI, record_resp):
    resp = api.security('NL0011540547').presentation().requests()
    check_has_fields(
        resp,
        must={
            'marketHours',
            'security',
            'socialInfo',
            'pendingOrders',
            'forexQuote',
        },
        maybe={'position'},
    )
    today = datetime.now().date()
    assert resp.market_hours.closing.date() <= today
    assert resp.ticker_code == 'ABN'
    print(resp['position'])
    check_has_all_getters(
        resp,
        exclude={'pendingOrders', 'forexQuote', 'stats'},
        unwrap={'security', 'socialInfo'},
    )
    check_has_all_getters(resp.market_hours)
    check_has_all_getters(resp.tags[0])


def test_security_presentation_etf(api: bux.UserAPI, record_resp):
    resp = api.security('NL0009272749').presentation().requests()
    fields = {'marketHours', 'security', 'socialInfo', 'pendingOrders', 'forexQuote'}
    assert set(resp) == fields
    today = datetime.now().date()
    assert resp.market_hours.closing.date() <= today
    assert resp.ticker_code == 'TDT'
    check_has_all_getters(
        resp,
        exclude={'pendingOrders', 'forexQuote', 'stats'},
        unwrap={'security', 'socialInfo'},
    )
    check_has_all_getters(resp.market_hours)
    check_has_all_getters(resp.tags[0])


def test_security_orders_config(api: bux.UserAPI, record_resp):
    resp = api.security('NL0009272749').orders_config().requests()
    fields = {
        'availableCash',
        'availableQuantity',
        'bid',
        'clientOrderTypes',
        'forexQuote',
        'offer',
        'shareLimit',
        'taxRate',
        'valueLimit',
    }
    assert set(resp) == fields
    check_has_all_getters(resp, exclude={'forexQuote', 'clientOrderTypes'})
