from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .transfer_order_created_event_object import TransferOrderCreatedEventObject, TransferOrderCreatedEventObjectDict


class TransferOrderCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"transfer_order"``."""

    id: Optional[str] = UNSET
    """ID of the affected transfer_order."""

    object_: Optional[TransferOrderCreatedEventObject] = Field(default=UNSET, alias="object")


class TransferOrderCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[TransferOrderCreatedEventObjectDict]
