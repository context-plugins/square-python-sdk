from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .payout_paid_event_object import PayoutPaidEventObject, PayoutPaidEventObjectDict


class PayoutPaidEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"payout"``."""

    id: Optional[str] = UNSET
    """ID of the completed payout."""

    object_: Optional[PayoutPaidEventObject] = Field(default=UNSET, alias="object")


class PayoutPaidEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[PayoutPaidEventObjectDict]
