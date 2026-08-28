from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.order_state import OrderStateOrStr


class SearchOrdersStateFilter(SdkBaseModel):
    """Filter by the current order ``state``."""

    states: list[OrderStateOrStr]
    """States to filter for. See `OrderState <#type-orderstate>`__ for possible values"""


class SearchOrdersStateFilterDict(TypedDict):
    states: list[OrderStateOrStr]
