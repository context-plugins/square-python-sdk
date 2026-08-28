from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.v1_update_order_request_action import V1UpdateOrderRequestActionOrStr


class V1UpdateOrderRequest(SdkBaseModel):
    """V1UpdateOrderRequest"""

    action: V1UpdateOrderRequestActionOrStr
    shipped_tracking_number: OptionalNullable[str] = UNSET
    """The tracking number of the shipment associated with the order. Only valid if action is COMPLETE."""

    completed_note: OptionalNullable[str] = UNSET
    """A merchant-specified note about the completion of the order. Only valid if action is COMPLETE."""

    refunded_note: OptionalNullable[str] = UNSET
    """A merchant-specified note about the refunding of the order. Only valid if action is REFUND."""

    canceled_note: OptionalNullable[str] = UNSET
    """A merchant-specified note about the canceling of the order. Only valid if action is CANCEL."""


class V1UpdateOrderRequestDict(TypedDict):
    action: V1UpdateOrderRequestActionOrStr
    shipped_tracking_number: NotRequired[str | None]
    completed_note: NotRequired[str | None]
    refunded_note: NotRequired[str | None]
    canceled_note: NotRequired[str | None]
