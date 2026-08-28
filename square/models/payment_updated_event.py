from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .payment_updated_event_data import PaymentUpdatedEventData, PaymentUpdatedEventDataDict


class PaymentUpdatedEvent(SdkBaseModel):
    """Published when a `Payment <entity:Payment>`__ is updated. Typically the ``payment.status``, or
    ``card_details.status`` fields are updated as a payment is canceled, authorized, or completed."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents, ``"payment.updated"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """Timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[PaymentUpdatedEventData] = UNSET


class PaymentUpdatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[PaymentUpdatedEventData | PaymentUpdatedEventDataDict]
