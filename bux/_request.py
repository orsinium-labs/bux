from dataclasses import dataclass
from http import HTTPStatus
from typing import Any, Callable, Dict, Generic, Optional, TypeVar


T = TypeVar('T')


class HTTPError(Exception):
    status: HTTPStatus
    text: str

    def __init__(self, status: int, text: str) -> None:
        self.status = HTTPStatus(status)
        self.text = text


@dataclass
class Request(Generic[T]):
    url: str
    headers: Dict[str, str]

    method: str = 'GET'
    body: Optional[bytes] = None
    data: Optional[Dict[str, Any]] = None
    params: Optional[Dict[str, Any]] = None
    on_json: Optional[Callable[[Any], T]] = None
    on_status: Optional[Callable[[int], T]] = None

    def requests(self) -> T:
        import requests

        response = requests.request(
            method=self.method,
            url=self.url,
            data=self.body,
            json=self.data,
            params=self.params,
            headers=self.headers,
        )
        if response.status_code >= 300:
            raise HTTPError(response.status_code, response.text)
        if self.on_json:
            return self.on_json(response.json())
        if self.on_status:
            return self.on_status(response.status_code)
        return response.json()

    def httpx(self) -> T:
        import httpx

        response = httpx.request(
            method=self.method,
            url=self.url,
            content=self.body,  # type: ignore[arg-type]
            json=self.data,
            params=self.params,
            headers=self.headers,
        )
        if response.status_code >= 300:
            raise HTTPError(response.status_code, response.text)
        if self.on_json:
            return self.on_json(response.json())
        if self.on_status:
            return self.on_status(response.status_code)
        return response.json()

    async def aiohttp(self) -> T:
        import aiohttp

        async with aiohttp.ClientSession() as session:
            response = await session.request(
                method=self.method,
                url=self.url,
                data=self.body,
                json=self.data,
                params=self.params,
                headers=self.headers,
            )
        if response.status >= 300:
            raise HTTPError(response.status, await response.text())
        if self.on_json:
            return self.on_json(await response.json())
        if self.on_status:
            return self.on_status(response.status)
        return await response.json()
