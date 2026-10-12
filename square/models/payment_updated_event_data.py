from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .payment_updated_event_object import PaymentUpdatedEventObject, PaymentUpdatedEventObjectDict


class PaymentUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"payment"``."""

    id: Optional[str] = UNSET
    """ID of the affected payment."""

    object_: Optional[PaymentUpdatedEventObject] = Field(default=UNSET, alias="object")


class PaymentUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[PaymentUpdatedEventObjectDict]
