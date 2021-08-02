from typing import Any, Dict


class Response(Dict[str, Any]):
    def __repr__(self) -> str:
        r = super().__repr__()
        return f'{type(self).__name__}({r})'
