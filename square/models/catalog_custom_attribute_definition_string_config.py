from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CatalogCustomAttributeDefinitionStringConfig(SdkBaseModel):
    """Configuration associated with Custom Attribute Definitions of type ``STRING``."""

    enforce_uniqueness: OptionalNullable[bool] = UNSET
    """If true, each Custom Attribute instance associated with this Custom Attribute Definition must have a unique value
    within the seller's catalog. For example, this may be used for a value like a SKU that should not be duplicated
    within a seller's catalog. May not be modified after the definition has been created."""


class CatalogCustomAttributeDefinitionStringConfigDict(TypedDict):
    enforce_uniqueness: NotRequired[bool | None]
