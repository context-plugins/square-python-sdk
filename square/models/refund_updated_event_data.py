from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .refund_updated_event_object import RefundUpdatedEventObject, RefundUpdatedEventObjectDict


class RefundUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"refund"``."""

    id: Optional[str] = UNSET
    """ID of the affected refund."""

    object_: Optional[RefundUpdatedEventObject] = Field(default=UNSET, alias="object")


class RefundUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[RefundUpdatedEventObject | RefundUpdatedEventObjectDict]
