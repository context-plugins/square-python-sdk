from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FilterValue(SdkBaseModel):
    """A filter to select resources based on an exact field value. For any given value, the value can only be in one
    property. Depending on the field, either all properties can be set or only a subset will be available.

    Refer to the documentation of the field."""

    all: OptionalNullable[list[str]] = UNSET
    """A list of terms that must be present on the field of the resource."""

    any: OptionalNullable[list[str]] = UNSET
    """A list of terms where at least one of them must be present on the field of the resource."""

    none: OptionalNullable[list[str]] = UNSET
    """A list of terms that must not be present on the field the resource"""


class FilterValueDict(TypedDict):
    all: NotRequired[list[str] | None]
    any: NotRequired[list[str] | None]
    none: NotRequired[list[str] | None]
