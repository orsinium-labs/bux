from pathlib import Path

import pytest

import bux


token = (Path(__file__).parent.parent / '.token').read_text().strip()


@pytest.fixture
def api() -> bux.UserAPI:
    return bux.UserAPI(token=token)
