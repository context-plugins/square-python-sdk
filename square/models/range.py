from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Range(SdkBaseModel):
    """The range of a number value between the specified lower and upper bounds."""

    min: OptionalNullable[str] = UNSET
    """The lower bound of the number range. At least one of ``min`` or ``max`` must be specified. If unspecified, the
    results will have no minimum value."""

    max: OptionalNullable[str] = UNSET
    """The upper bound of the number range. At least one of ``min`` or ``max`` must be specified. If unspecified, the
    results will have no maximum value."""


class RangeDict(TypedDict):
    min: NotRequired[str | None]
    max: NotRequired[str | None]
