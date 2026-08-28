from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class InvoiceDeletedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"invoice"``."""

    id: Optional[str] = UNSET
    """ID of the affected invoice."""

    deleted: OptionalNullable[bool] = UNSET
    """Indicates that the invoice was deleted."""


class InvoiceDeletedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    deleted: NotRequired[bool | None]
