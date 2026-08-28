from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LoyaltyEventOrderFilter(SdkBaseModel):
    """Filter events by the order associated with the event."""

    order_id: str
    """The ID of the `order <entity:Order>`__ associated with the event."""


class LoyaltyEventOrderFilterDict(TypedDict):
    order_id: str
