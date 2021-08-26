"""Unofficial SDK and CLI for BUX Zero API.

https://getbux.com/
"""

from . import types
from ._guest import GuestAPI
from ._request import HTTPError, Request
from ._user import UserAPI
from ._ws import WebSocketAPI
from .types import Response


__version__ = '0.2.0'
__all__ = [
    'GuestAPI',
    'HTTPError',
    'Request',
    'UserAPI',
    'Response',
    'WebSocketAPI',
    'types',
]
