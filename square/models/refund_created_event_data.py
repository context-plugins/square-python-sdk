from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .refund_created_event_object import RefundCreatedEventObject, RefundCreatedEventObjectDict


class RefundCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"refund"``."""

    id: Optional[str] = UNSET
    """ID of the affected refund."""

    object_: Optional[RefundCreatedEventObject] = Field(default=UNSET, alias="object")


class RefundCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[RefundCreatedEventObjectDict]
