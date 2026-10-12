from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .invoice_payment_made_event_object import InvoicePaymentMadeEventObject, InvoicePaymentMadeEventObjectDict


class InvoicePaymentMadeEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"invoice"``."""

    id: Optional[str] = UNSET
    """ID of the affected invoice."""

    object_: Optional[InvoicePaymentMadeEventObject] = Field(default=UNSET, alias="object")


class InvoicePaymentMadeEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[InvoicePaymentMadeEventObjectDict]
