from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .catalog_object import CatalogObject, CatalogObjectDict


class CatalogItemOption(SdkBaseModel):
    """A group of variations for a ``CatalogItem``."""

    name: OptionalNullable[str] = UNSET
    """The item option's display name for the seller. Must be unique across all item options. This is a searchable
    attribute for use in applicable query filters."""

    display_name: OptionalNullable[str] = UNSET
    """The item option's display name for the customer. This is a searchable attribute for use in applicable query
    filters."""

    description: OptionalNullable[str] = UNSET
    """The item option's human-readable description. Displayed in the Square Point of Sale app for the seller and in the
    Online Store or on receipts for the buyer. This is a searchable attribute for use in applicable query filters."""

    show_colors: OptionalNullable[bool] = UNSET
    """If true, display colors for entries in ``values`` when present."""

    values: OptionalNullable[list[CatalogObject]] = UNSET
    """A list of CatalogObjects containing the ``CatalogItemOptionValue``s for this item."""


class CatalogItemOptionDict(TypedDict):
    name: NotRequired[str | None]
    display_name: NotRequired[str | None]
    description: NotRequired[str | None]
    show_colors: NotRequired[bool | None]
    values: NotRequired[list[CatalogObjectDict] | None]
