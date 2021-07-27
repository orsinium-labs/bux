import bux
import pytest
from pathlib import Path


token = (Path(__file__).parent.parent / '.token').read_text().strip()


@pytest.fixture
def api() -> bux.UserAPI:
    return bux.UserAPI(token=token)
