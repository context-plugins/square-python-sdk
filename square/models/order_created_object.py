from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order_created import OrderCreated, OrderCreatedDict


class OrderCreatedObject(SdkBaseModel):
    order_created: Optional[OrderCreated] = UNSET


class OrderCreatedObjectDict(TypedDict):
    order_created: NotRequired[OrderCreatedDict]
