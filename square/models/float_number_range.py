from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FloatNumberRange(SdkBaseModel):
    """Specifies a decimal number range."""

    start_at: OptionalNullable[str] = UNSET
    """A decimal value indicating where the range starts."""

    end_at: OptionalNullable[str] = UNSET
    """A decimal value indicating where the range ends."""


class FloatNumberRangeDict(TypedDict):
    start_at: NotRequired[str | None]
    end_at: NotRequired[str | None]
