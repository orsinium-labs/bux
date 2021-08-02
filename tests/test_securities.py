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
    check_has_all_getters(resp.value_filters[0])
    check_has_all_getters(resp.toggle_filters[0])


def test_securities_featured_tags(api: bux.UserAPI, record_resp):
    resp = api.securities().featured_tags().requests()
    fields = {'id', 'name', 'type', 'iconLarge', 'iconSmall'}
    assert set(resp[0]) == fields
    check_has_all_getters(resp[0])


def test_securities_countries(api: bux.UserAPI, record_resp):
    resp = api.securities().countries().requests()
    fields = {'id', 'name', 'type', 'iconLarge', 'iconSmall'}
    assert set(resp[0]) == fields
    check_has_all_getters(resp[0])
    assert resp[0].name == 'Austria'
    assert resp[0].id == 'AT'
    assert resp[0].type == 'Country'
