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
