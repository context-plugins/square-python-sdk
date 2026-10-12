from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .invoice_scheduled_charge_failed_event_data import (
    InvoiceScheduledChargeFailedEventData,
    InvoiceScheduledChargeFailedEventDataDict,
)


class InvoiceScheduledChargeFailedEvent(SdkBaseModel):
    """Published when an automatic scheduled payment for an `Invoice <entity:Invoice>`__ has failed."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents, ``"invoice.scheduled_charge_failed"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """Timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[InvoiceScheduledChargeFailedEventData] = UNSET


class InvoiceScheduledChargeFailedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[InvoiceScheduledChargeFailedEventDataDict]
