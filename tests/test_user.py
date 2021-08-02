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
