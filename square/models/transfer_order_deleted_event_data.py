from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TransferOrderDeletedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"transfer_order"``."""

    id: Optional[str] = UNSET
    """ID of the affected transfer_order."""

    deleted: OptionalNullable[bool] = UNSET
    """Is true if the affected object was deleted. Otherwise absent."""


class TransferOrderDeletedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    deleted: NotRequired[bool | None]
