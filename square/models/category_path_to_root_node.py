from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CategoryPathToRootNode(SdkBaseModel):
    """A node in the path from a retrieved category to its root node."""

    category_id: OptionalNullable[str] = UNSET
    """The category's ID."""

    category_name: OptionalNullable[str] = UNSET
    """The category's name."""


class CategoryPathToRootNodeDict(TypedDict):
    category_id: NotRequired[str | None]
    category_name: NotRequired[str | None]
