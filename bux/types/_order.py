from datetime import datetime
from typing import List

from ._orders_config import ExecutionWindow
from ._price import Price
from ._response import Response


class Order(Response):  # pragma: no cover
    @property
    def created_date(self) -> datetime:
        return datetime.fromtimestamp(self['createdDate'] / 1000)

    @property
    def direction(self) -> str:
        """`BUY` or `SELL`
        """
        return self['direction']

    @property
    def execution_windows(self) -> List[ExecutionWindow]:
        return [ExecutionWindow(w) for w in self['executionWindows']]

    @property
    def fee_estimate(self) -> Price:
        return Price(self['feeEstimate'])

    @property
    def id(self) -> str:
        """UUID of the order.
        """
        return self['id']

    @property
    def is_cancellable(self) -> bool:
        return self['isCancellable']

    @property
    def quantity(self) -> int:
        return self['quantity']

    @property
    def security_id(self) -> str:
        """Example: `IE00B3XXRP09`
        """
        return self['isin']

    @property
    def security_type(self) -> str:
        """`EQTY` or `ETF`
        """
        return self['securityType']

    @property
    def type(self) -> str:
        """`BASIC`, `MARKET`, or `LIMIT_ORDER_1D`.
        """
        return self['type']
