from ._response import Response


class Tag(Response):
    @property
    def name(self) -> str:
        return self['name']

    @property
    def id(self) -> str:
        return self['id']

    @property
    def type(self) -> str:
        return self['type']

    @property
    def icon_small(self) -> str:
        return self['iconSmall']

    @property
    def icon_large(self) -> str:
        return self['iconLarge']
