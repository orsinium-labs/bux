from typing import NamedTuple, NewType, Optional, Type, TypeVar
from contextlib import asynccontextmanager

from ._config import Config
import json
from websockets.legacy.client import Connect, WebSocketClientProtocol
from . import types

T = TypeVar('T', bound='WebSocketAPI')
Topic = NewType('Topic', str)


class Topics:
    badge = Topic('users.me.badge')
    cash_balance = Topic('users.me.cashBalance')
    comm_config = Topic('users.me.configuration.communication')
    followed_securities = Topic('users.me.securities')
    inbox = Topic('users.me.inbox')
    logbook = Topic('users.me.logbook')
    market = Topic('stocks.market')
    onboarding = Topic('users.me.onboarding')
    orders = Topic('users.me.orders')
    portfolio = Topic('users.me.portfolio.v2')
    trades = Topic('users.me.trades')
    user_status = Topic('users.me.status')

    @staticmethod
    def forex(ticker: str) -> Topic:
        return Topic(f'forex.quote.{ticker}')

    @staticmethod
    def security(ticker: str) -> Topic:
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

    async def __anext__(self) -> types.WSResponse:
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

    async def get(self) -> types.WSResponse:
        if self.connection is None:
            raise RuntimeError("WebSocketAPI is not connected")
        raw = await self.connection.recv()
        msg = json.loads(raw)
        if msg['t'] == 'stocks.quote':
            return types.WSQuote(msg['body'])
        return types.WSResponse(msg['body'])

    @asynccontextmanager
    async def listen(self, *topics: Topic):
        await self.subscribe(*topics)
        try:
            yield self
        finally:
            await self.unsubscribe(*topics)
