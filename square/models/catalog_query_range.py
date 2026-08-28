from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CatalogQueryRange(SdkBaseModel):
    """The query filter to return the search result whose named attribute values fall between the specified range."""

    attribute_name: str
    """The name of the attribute to be searched."""

    attribute_min_value: OptionalNullable[int] = UNSET
    """The desired minimum value for the search attribute (inclusive)."""

    attribute_max_value: OptionalNullable[int] = UNSET
    """The desired maximum value for the search attribute (inclusive)."""


class CatalogQueryRangeDict(TypedDict):
    attribute_name: str
    attribute_min_value: NotRequired[int | None]
    attribute_max_value: NotRequired[int | None]
