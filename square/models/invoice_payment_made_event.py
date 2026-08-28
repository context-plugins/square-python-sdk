from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .invoice_payment_made_event_data import InvoicePaymentMadeEventData, InvoicePaymentMadeEventDataDict


class InvoicePaymentMadeEvent(SdkBaseModel):
    """Published when a payment that is associated with an `invoice <entity:Invoice>`__ is completed. For more
    information about invoice payments, see `Pay an invoice
    <https://developer.squareup.com/docs/invoices-api/pay-refund-invoices#pay-invoice>`__."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents, ``"invoice.payment_made"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """Timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[InvoicePaymentMadeEventData] = UNSET


class InvoicePaymentMadeEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[InvoicePaymentMadeEventData | InvoicePaymentMadeEventDataDict]
