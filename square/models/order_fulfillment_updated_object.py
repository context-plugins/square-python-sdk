from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order_fulfillment_updated import OrderFulfillmentUpdated, OrderFulfillmentUpdatedDict


class OrderFulfillmentUpdatedObject(SdkBaseModel):
    order_fulfillment_updated: Optional[OrderFulfillmentUpdated] = UNSET


class OrderFulfillmentUpdatedObjectDict(TypedDict):
    order_fulfillment_updated: NotRequired[OrderFulfillmentUpdated | OrderFulfillmentUpdatedDict]
