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
