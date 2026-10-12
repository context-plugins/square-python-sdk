from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .payment_created_event_object import PaymentCreatedEventObject, PaymentCreatedEventObjectDict


class PaymentCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"payment"``."""

    id: Optional[str] = UNSET
    """ID of the affected payment."""

    object_: Optional[PaymentCreatedEventObject] = Field(default=UNSET, alias="object")


class PaymentCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[PaymentCreatedEventObjectDict]
