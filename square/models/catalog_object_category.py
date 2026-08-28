from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CatalogObjectCategory(SdkBaseModel):
    """A category that can be assigned to an item or a parent category that can be assigned to another category. For
    example, a clothing category can be assigned to a t-shirt item or be made as the parent category to the pants
    category."""

    id: Optional[str] = UNSET
    """The ID of the object's category."""

    ordinal: OptionalNullable[int] = UNSET
    """The position of this object within the specified category. When an item is assigned to a category, the ordinal
    determines the item's position relative to other items in the same category. When used for a parent category
    reference, the ordinal determines the category's position among its sibling categories."""


class CatalogObjectCategoryDict(TypedDict):
    id: NotRequired[str]
    ordinal: NotRequired[int | None]
