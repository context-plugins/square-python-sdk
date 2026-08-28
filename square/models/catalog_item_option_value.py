from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CatalogItemOptionValue(SdkBaseModel):
    """An enumerated value that can link a ``CatalogItemVariation`` to an item option as one of its item option
    values."""

    item_option_id: OptionalNullable[str] = UNSET
    """Unique ID of the associated item option."""

    name: OptionalNullable[str] = UNSET
    """Name of this item option value. This is a searchable attribute for use in applicable query filters."""

    description: OptionalNullable[str] = UNSET
    """A human-readable description for the option value. This is a searchable attribute for use in applicable query
    filters."""

    color: OptionalNullable[str] = UNSET
    """The HTML-supported hex color for the item option (e.g., "#ff8d4e85"). Only displayed if ``show_colors`` is
    enabled on the parent ``ItemOption``. When left unset, ``color`` defaults to white ("#ffffff") when ``show_colors``
    is enabled on the parent ``ItemOption``."""

    ordinal: OptionalNullable[int] = UNSET
    """Determines where this option value appears in a list of option values."""


class CatalogItemOptionValueDict(TypedDict):
    item_option_id: NotRequired[str | None]
    name: NotRequired[str | None]
    description: NotRequired[str | None]
    color: NotRequired[str | None]
    ordinal: NotRequired[int | None]
