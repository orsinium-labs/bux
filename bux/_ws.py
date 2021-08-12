from typing import NamedTuple, NewType, Optional, Type, TypeVar
from contextlib import asynccontextmanager

from ._config import Config
import json
from websockets.legacy.client import Connect, WebSocketClientProtocol
from . import types

T = TypeVar('T', bound='WebSocketAPI')
Topic = NewType('Topic', str)


class Topics:
    my_status = Topic('users.me.status')
    my_badge = Topic('users.me.badge')
    my_inbox = Topic('users.me.inbox')
    my_orders = Topic('users.me.orders')
    my_portfolio = Topic('users.me.portfolio')
    market = Topic('stocks.market')

    @staticmethod
    def quote(ticker: str) -> Topic:
        return Topic(f'stocks.quote.{ticker}')


class WebSocketAPI(NamedTuple):
    token: str
    config: Config = Config()
    connection: Optional[WebSocketClientProtocol] = None
    topics: Type[Topics] = Topics

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

    async def subscribe(self, *topics: Topic) -> None:
        await self._send(
            subscribeTo=topics,
            unsubscribeFrom=[],
        )

    async def unsubscribe(self, *topics: Topic) -> None:
        await self._send(
            subscribeTo=[],
            unsubscribeFrom=topics,
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
    async def listen(self, *topics: Topic):
        await self.subscribe(*topics)
        try:
            yield self
        finally:
            await self.unsubscribe(*topics)
