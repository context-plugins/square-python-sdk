from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.sort_order import SortOrderOrStr


class CatalogQuerySortedAttribute(SdkBaseModel):
    """The query expression to specify the key to sort search results."""

    attribute_name: str
    """The attribute whose value is used as the sort key."""

    initial_attribute_value: OptionalNullable[str] = UNSET
    """The first attribute value to be returned by the query. Ascending sorts will return only objects with this value
    or greater, while descending sorts will return only objects with this value or less. If unset, start at the
    beginning (for ascending sorts) or end (for descending sorts)."""

    sort_order: Optional[SortOrderOrStr] = UNSET
    """The order (e.g., chronological or alphabetical) in which results from a request are returned."""


class CatalogQuerySortedAttributeDict(TypedDict):
    attribute_name: str
    initial_attribute_value: NotRequired[str | None]
    sort_order: NotRequired[SortOrderOrStr]
