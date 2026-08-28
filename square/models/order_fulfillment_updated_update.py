from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.fulfillment_state import FulfillmentStateOrStr


class OrderFulfillmentUpdatedUpdate(SdkBaseModel):
    """Information about fulfillment updates."""

    fulfillment_uid: OptionalNullable[str] = UNSET
    """A unique ID that identifies the fulfillment only within this order."""

    old_state: Optional[FulfillmentStateOrStr] = UNSET
    """The current state of this fulfillment."""

    new_state: Optional[FulfillmentStateOrStr] = UNSET
    """The current state of this fulfillment."""


class OrderFulfillmentUpdatedUpdateDict(TypedDict):
    fulfillment_uid: NotRequired[str | None]
    old_state: NotRequired[FulfillmentStateOrStr]
    new_state: NotRequired[FulfillmentStateOrStr]
