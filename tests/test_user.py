import bux

from .helpers import check_has_all_getters


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
    check_has_all_getters(resp, exclude={'positions'})
    if resp['positions']['EQTY']:
        check_has_all_getters(
            resp.positions_eqty[0],
            exclude={'securityType', 'position'},
            unwrap={'security'},
        )


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


def test_inbox(api: bux.UserAPI, record_resp):
    resp = api.inbox().requests()
    assert resp
    fields = {'id', 'timestamp', 'type', 'unread', 'content'}
    assert set(resp[0]) == fields
    assert resp[0].type.isupper()
    for msg in resp:
        check_has_all_getters(msg, unwrap={'content'})


def test_search(api: bux.UserAPI, record_resp):
    resp = api.search('Netherlands').requests()
    fields = {'securities', 'tags', 'securitiesUnderPrice'}
    assert set(resp) == fields
    assert resp.tags
    for tag in resp.tags:
        check_has_all_getters(tag)

    assert resp.etf
    for etf in resp.etf:
        check_has_all_getters(
            etf,
            unwrap={'security', 'socialInfo'},
            exclude={'stats'},
        )
