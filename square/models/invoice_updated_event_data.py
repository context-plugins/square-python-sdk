from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .invoice_updated_event_object import InvoiceUpdatedEventObject, InvoiceUpdatedEventObjectDict


class InvoiceUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"invoice"``."""

    id: Optional[str] = UNSET
    """ID of the affected invoice."""

    object_: Optional[InvoiceUpdatedEventObject] = Field(default=UNSET, alias="object")


class InvoiceUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[InvoiceUpdatedEventObjectDict]
