from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CatalogItemOptionForItem(SdkBaseModel):
    """An option that can be assigned to an item. For example, a t-shirt item may offer a color option or a size
    option."""

    item_option_id: OptionalNullable[str] = UNSET
    """The unique id of the item option, used to form the dimensions of the item option matrix in a specified order."""


class CatalogItemOptionForItemDict(TypedDict):
    item_option_id: NotRequired[str | None]
