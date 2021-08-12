from typing import NamedTuple, Optional, TypeVar
from contextlib import asynccontextmanager

from ._config import Config
import json
from websockets.legacy.client import Connect, WebSocketClientProtocol
from . import types

T = TypeVar('T', bound='WebSocketAPI')


TOPICS = {
    "users.me.status",
    "users.me.badge",
    "users.me.inbox",
    "users.me.orders",
    "users.me.portfolio.v2",
    "stocks.market",
}


class WebSocketAPI(NamedTuple):
    token: str
    config: Config = Config()
    connection: Optional[WebSocketClientProtocol] = None

    async def _send(self, **kwargs) -> None:
        if self.connection is None:
            raise RuntimeError("WebSocketAPI is not connected")
        await self.connection.send(json.dumps(kwargs))

    async def __aenter__(self: T) -> T:
        return self._replace(connection=await Connect(
            uri=self.config.ws_url,
            extra_headers={
                'authorization': f'Bearer {self.token}',
                'pin-authorization': 'Bearer null',
                **self.config.headers,
            },
        ))

    def __aiter__(self: T) -> T:
        return self

    async def __anext__(self) -> types.Response:
        return await self.get()

    async def __aexit__(self, *args, **kwargs) -> None:
        assert self.connection is not None
        await self.connection.close()

    async def subscribe(self, topic: str):
        await self._send(
            subscribeTo=[topic],
            unsubscribeFrom=[],
        )

    async def unsubscribe(self, topic: str):
        await self._send(
            subscribeTo=[],
            unsubscribeFrom=[topic],
        )

    async def get(self) -> types.Response:
        if self.connection is None:
            raise RuntimeError("WebSocketAPI is not connected")
        raw = await self.connection.recv()
        msg = json.loads(raw)
        if msg['t'] == 'stocks.quote':
            return types.WSQuote(msg['body'])
        return types.Response(msg['body'])

    @asynccontextmanager
    async def quote(self, ticker: str):
        topic = f'stocks.quote.{ticker}'
        await self.subscribe(topic)
        try:
            yield self
        finally:
            await self.unsubscribe(topic)
