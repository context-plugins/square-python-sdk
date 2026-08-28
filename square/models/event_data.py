from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class EventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The name of the affected object’s type."""

    id: Optional[str] = UNSET
    """The ID of the affected object."""

    deleted: OptionalNullable[bool] = UNSET
    """This is true if the affected object has been deleted; otherwise, it's absent."""

    object_: OptionalNullable[Any] = Field(default=UNSET, alias="object")
    """An object containing fields and values relevant to the event. It is absent if the affected object has been
    deleted."""


class EventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    deleted: NotRequired[bool | None]
    object_: NotRequired[Any | None]
