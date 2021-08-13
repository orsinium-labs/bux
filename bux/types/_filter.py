from typing import Optional

from ._response import Response


class Filter(Response):
    @property
    def name(self) -> str:
        return self['displayName']

    @property
    def enabled(self) -> bool:
        return self.get('isEnabled', True)

    @property
    def type(self) -> str:
        return self['type']

    @property
    def value(self) -> Optional[str]:
        return self.get('value')
