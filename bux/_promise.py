from typing import Any, Callable, Dict, Generic, Optional, TypeVar
from dataclasses import dataclass
import aiohttp
import requests


T = TypeVar('T')


@dataclass
class Promise(Generic[T]):
    method: str
    url: str
    headers: Dict[str, str]

    data: Optional[Dict[str, Any]] = None
    on_json: Optional[Callable[[Any], T]] = None
    on_status: Optional[Callable[[int], T]] = None

    def requests(self) -> T:
        response = requests.request(
            method=self.method,
            url=self.url,
            json=self.data,
        )
        response.raise_for_status()
        if self.on_json:
            return self.on_json(response.json())
        if self.on_status:
            return self.on_status(response.status_code)
        return response.json()

    async def aiohttp(self) -> T:
        async with aiohttp.ClientSession() as session:
            response = await session.request(
                method=self.method,
                url=self.url,
                json=self.data,
            )
        response.raise_for_status()
        if self.on_json:
            return self.on_json(await response.json())
        if self.on_status:
            return self.on_status(response.status)
        return await response.json()
