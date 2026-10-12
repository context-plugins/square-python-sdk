from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .invoice_scheduled_charge_failed_event_object import (
    InvoiceScheduledChargeFailedEventObject,
    InvoiceScheduledChargeFailedEventObjectDict,
)


class InvoiceScheduledChargeFailedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"invoice"``."""

    id: Optional[str] = UNSET
    """ID of the affected invoice."""

    object_: Optional[InvoiceScheduledChargeFailedEventObject] = Field(default=UNSET, alias="object")


class InvoiceScheduledChargeFailedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[InvoiceScheduledChargeFailedEventObjectDict]
