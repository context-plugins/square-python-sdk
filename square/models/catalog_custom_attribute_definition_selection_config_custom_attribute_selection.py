from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelection(SdkBaseModel):
    """A named selection for this ``SELECTION``-type custom attribute definition."""

    uid: OptionalNullable[str] = UNSET
    """Unique ID set by Square."""

    name: str
    """Selection name, unique within ``allowed_selections``."""


class CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelectionDict(TypedDict):
    uid: NotRequired[str | None]
    name: str
