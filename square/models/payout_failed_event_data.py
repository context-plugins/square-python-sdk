from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .payout_failed_event_object import PayoutFailedEventObject, PayoutFailedEventObjectDict


class PayoutFailedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The name of the affected object's type, ``payout``."""

    id: Optional[str] = UNSET
    """The ID of the failed payout."""

    object_: Optional[PayoutFailedEventObject] = Field(default=UNSET, alias="object")


class PayoutFailedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[PayoutFailedEventObjectDict]
