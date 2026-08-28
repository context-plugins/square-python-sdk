from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .invoice_published_event_data import InvoicePublishedEventData, InvoicePublishedEventDataDict


class InvoicePublishedEvent(SdkBaseModel):
    """Published when an `Invoice <entity:Invoice>`__ transitions from a draft to a non-draft status."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents, ``"invoice.published"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """Timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[InvoicePublishedEventData] = UNSET


class InvoicePublishedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[InvoicePublishedEventData | InvoicePublishedEventDataDict]
