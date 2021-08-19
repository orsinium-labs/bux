import io

from bux._cli import main


def _call(*cmd: str, token, code=0) -> str:
    stream = io.StringIO()
    cmd += ('--token', token)
    actual_code = main(list(cmd), stream=stream)
    assert actual_code == code
    stream.seek(0)
    return stream.read()


def test_cli_countries(token, record_resp):
    result = _call('countries', token=token)
    assert 'NL' in result
    assert 'Netherlands' in result


def test_cli_search(token, record_resp):
    result = _call('search', 'gopro', token=token)
    assert 'GoPro' in result
    assert 'GPRO' in result
    assert 'US38268T1034' in result


def test_cli_info(token, record_resp):
    result = _call('info', 'US38268T1034', token=token)
    assert 'bid' in result
    assert 'GPRO' in result
    assert 'GoPro' in result
    assert 'Nick Woodman' in result
    assert 'USD' in result
    assert '5d' in result


def test_cli_me(token, record_resp):
    result = _call('me', token=token)
    assert '@' in result
    assert '.' in result


def test_cli_categories(token, record_resp):
    result = _call('categories', token=token)
    assert 'real-estate' in result
    assert 'finance' in result


def test_cli_inbox(token, record_resp):
    result = _call('inbox', token=token)
    assert 'Welcome to BUX Zero' in result
    assert 'Create your account now' in result


def test_cli_tags(token, record_resp):
    result = _call('tags', 'NL', token=token)
    assert 'communication' in result
    assert 'real-estate' in result


def test_cli_tag(token, record_resp):
    result = _call('tag', 'NL', token=token)
    assert 'PostNL' in result
    assert 'NL0009739416' in result
    assert 'PNL' in result


def test_cli_gainers(token, record_resp):
    result = _call('gainers', token=token)
    assert '+' in result
    assert '%' in result
    assert '00' in result


def test_cli_losers(token, record_resp):
    result = _call('losers', token=token)
    assert '-' in result
    assert '%' in result
    assert '00' in result


def test_cli_new_stocks(token, record_resp):
    result = _call('new-stocks', token=token)
    assert 'ETF' in result
    assert '00' in result


def test_cli_following(token, record_resp):
    result = _call('following', token=token)
    assert '%' in result
    assert '00' in result


def test_cli_graph(token, record_resp):
    result = _call('graph', 'US38268T1034', token=token)
    assert '.' in result
    assert ' ' in result
    assert '-' in result
    assert ':00' in result


def test_cli_orders_config(token, record_resp):
    result = _call('orders-config', 'NL0011540547', token=token)
    assert 'BASIC:' in result
    assert 'MARKET:' in result
    assert 'LIMIT_ORDER_1D:' in result
    assert 'expires' in result
    assert 'fee 1.00 EUR' in result
    assert '09:00:00' in result
    assert '17:30:00' in result
