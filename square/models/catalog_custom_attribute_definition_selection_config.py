from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .catalog_custom_attribute_definition_selection_config_custom_attribute_selection import (
    CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelection,
    CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelectionDict,
)


class CatalogCustomAttributeDefinitionSelectionConfig(SdkBaseModel):
    """Configuration associated with ``SELECTION``-type custom attribute definitions."""

    max_allowed_selections: OptionalNullable[int] = UNSET
    """The maximum number of selections that can be set. The maximum value for this attribute is 100. The default value
    is 1. The value can be modified, but changing the value will not affect existing custom attribute values on objects.
    Clients need to handle custom attributes with more selected values than allowed by this limit."""

    allowed_selections: Optional[
        list[CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelection | None]
    ] = UNSET
    """The set of valid ``CatalogCustomAttributeSelections``. Up to a maximum of 100 selections can be defined. Can be
    modified."""


class CatalogCustomAttributeDefinitionSelectionConfigDict(TypedDict):
    max_allowed_selections: NotRequired[int | None]
    allowed_selections: NotRequired[
        list[
            (
                CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelection
                | CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelectionDict
                | None
            )
        ]
    ]
