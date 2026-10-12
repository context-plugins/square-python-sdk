from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .order_updated_object import OrderUpdatedObject, OrderUpdatedObjectDict


class OrderUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"order_updated"``."""

    id: Optional[str] = UNSET
    """ID of the affected order."""

    object_: Optional[OrderUpdatedObject] = Field(default=UNSET, alias="object")


class OrderUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[OrderUpdatedObjectDict]
