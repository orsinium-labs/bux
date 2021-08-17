from pathlib import Path

import pytest
from _pytest.fixtures import FixtureRequest
from vcr import VCR

import bux


ROOT = Path(__file__).parent.parent


@pytest.fixture(scope='session')
def token():
    return (ROOT / '.token').read_text().strip()


@pytest.fixture(scope='session')
def pin():
    return (ROOT / '.pin').read_text().strip()


@pytest.fixture
def api(token) -> bux.UserAPI:
    return bux.UserAPI(token=token)


@pytest.fixture
def record_resp(request: FixtureRequest):
    path = ROOT / 'tests' / 'cassettes' / f'{request.node.name}.yaml'
    vcr = VCR(serializer='yaml')
    with vcr.use_cassette(str(path)):
        yield
