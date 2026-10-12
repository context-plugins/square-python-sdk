from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .order_created_object import OrderCreatedObject, OrderCreatedObjectDict


class OrderCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"order_created"``."""

    id: Optional[str] = UNSET
    """ID of the affected order."""

    object_: Optional[OrderCreatedObject] = Field(default=UNSET, alias="object")


class OrderCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[OrderCreatedObjectDict]
