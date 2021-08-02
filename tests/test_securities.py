import bux

from .helpers import check_has_all_getters


def test_securities_movers(api: bux.UserAPI, record_resp):
    resp = api.securities().movers().requests()
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
    check_has_all_getters(resp.gainers[0], unwrap={'stats'})
    check_has_all_getters(resp.losers[0], unwrap={'stats'})

    assert len(resp.value_filters) >= 1
    for tag in resp.value_filters:
        check_has_all_getters(tag)

    assert len(resp.toggle_filters) >= 1
    for tag in resp.toggle_filters:
        check_has_all_getters(tag)


def test_securities_featured_tags(api: bux.UserAPI, record_resp):
    resp = api.securities().featured_tags().requests()
    fields = {'id', 'name', 'type', 'iconLarge', 'iconSmall'}
    assert set(resp[0]) == fields
    assert len(resp) >= 10
    for tag in resp:
        check_has_all_getters(tag)


def test_securities_countries(api: bux.UserAPI, record_resp):
    resp = api.securities().countries().requests()
    fields = {'id', 'name', 'type', 'iconLarge', 'iconSmall'}
    assert set(resp[0]) == fields
    assert len(resp) == 6
    for country in resp:
        check_has_all_getters(country)
    assert resp[0].name == 'Austria'
    assert resp[0].id == 'AT'
    assert resp[0].type == 'Country'


def test_securities_etfs(api: bux.UserAPI, record_resp):
    resp = api.securities().etfs().requests()
    fields = {
        'bid',
        'closingBid',
        'description',
        'id',
        'name',
        'offer',
        'openingBid',
        'securityType',
        'stats',
        'tickerCode',
    }
    assert len(resp) >= 1
    assert set(resp[0]) == fields
    check_has_all_getters(resp[0], unwrap={'stats'})


def test_securities_usa(api: bux.UserAPI, record_resp):
    resp = api.securities().usa().requests()
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
    assert len(resp) >= 1
    assert set(resp[0]) == fields
    check_has_all_getters(resp[0], unwrap={'stats'})


def test_securities_filter_tag(api: bux.UserAPI, record_resp):
    resp = api.securities().filter_tag('NL').requests()
    fields = {
        'tags',
        'parentTag',
        'stocks',
    }
    assert set(resp) == fields
    check_has_all_getters(resp)

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
    assert set(resp.stocks[0]) == fields
    check_has_all_getters(resp.stocks[0], unwrap={'stats'})
