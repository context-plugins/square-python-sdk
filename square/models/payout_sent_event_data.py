from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .payout_sent_event_object import PayoutSentEventObject, PayoutSentEventObjectDict


class PayoutSentEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"payout"``."""

    id: Optional[str] = UNSET
    """ID of the sent payout."""

    object_: Optional[PayoutSentEventObject] = Field(default=UNSET, alias="object")


class PayoutSentEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[PayoutSentEventObjectDict]
