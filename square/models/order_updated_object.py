from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order_updated import OrderUpdated, OrderUpdatedDict


class OrderUpdatedObject(SdkBaseModel):
    order_updated: Optional[OrderUpdated] = UNSET


class OrderUpdatedObjectDict(TypedDict):
    order_updated: NotRequired[OrderUpdatedDict]
