from datetime import datetime
from decimal import Decimal
from typing import Optional

import bux


def check_has_fields(real: dict, must: set, maybe: Optional[set] = None):
    actual = set(real) - (maybe or set())
    diff = actual - must
    assert not diff, f'Unexpected fields: {diff}'
    diff = must - actual
    assert not diff, f'Missed fields: {diff}'
    assert actual == must


def check_has_all_getters(resp: bux.Response, exclude=(), unwrap=()):
    values = []
    dict_attrs = dir(dict)
    for name in dir(type(resp)):
        if name in dict_attrs:
            continue
        if name.startswith('_'):
            continue
        value = getattr(resp, name)
        if isinstance(value, bux.Response):
            value = dict(value)
        if isinstance(value, Decimal):
            value = str(value)
        if isinstance(value, datetime):
            value = value.timestamp() * 1000
        values.append(value)

    missed = []
    for name, value in resp.items():
        if name in exclude:
            continue
        if name in unwrap:
            continue
        if isinstance(value, str) and value.isdigit():
            if int(value) in values:
                continue
        if value not in values:
            missed.append(name)
    for group in unwrap:
        for name, value in resp[group].items():
            if name in exclude:
                continue
            if name in unwrap:
                continue
            if value not in values:
                missed.append(name)
    assert not missed, 'Missed fields: ' + ', '.join(missed)
