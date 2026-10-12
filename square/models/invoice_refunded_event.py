from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .invoice_refunded_event_data import InvoiceRefundedEventData, InvoiceRefundedEventDataDict


class InvoiceRefundedEvent(SdkBaseModel):
    """Published when a refund is applied toward a payment of an `invoice <entity:Invoice>`__. For more information
    about invoice refunds, see `Refund an invoice
    <https://developer.squareup.com/docs/invoices-api/pay-refund-invoices#refund-invoice>`__."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents, ``"invoice.refunded"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """Timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[InvoiceRefundedEventData] = UNSET


class InvoiceRefundedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[InvoiceRefundedEventDataDict]
