from datetime import datetime
from typing import Optional

from ._response import Response


class Message(Response):
    @property
    def id(self) -> str:
        return self['id']

    @property
    def time(self) -> datetime:
        return datetime.fromtimestamp(self['timestamp'] / 1000)

    @property
    def type(self) -> str:
        return self['type']

    @property
    def unread(self) -> bool:
        return self['unread']

    @property
    def icon(self) -> str:
        return self['content']['icon']

    @property
    def image(self) -> Optional[str]:
        return self['content'].get('image')

    @property
    def link(self) -> Optional[str]:
        return self['content'].get('link')

    @property
    def title(self) -> str:
        return self['content']['title']

    @property
    def description(self) -> str:
        return self['content']['subtitle']
