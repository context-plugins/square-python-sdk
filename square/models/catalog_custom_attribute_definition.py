from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .catalog_custom_attribute_definition_number_config import (
    CatalogCustomAttributeDefinitionNumberConfig,
    CatalogCustomAttributeDefinitionNumberConfigDict,
)
from .catalog_custom_attribute_definition_selection_config import (
    CatalogCustomAttributeDefinitionSelectionConfig,
    CatalogCustomAttributeDefinitionSelectionConfigDict,
)
from .catalog_custom_attribute_definition_string_config import (
    CatalogCustomAttributeDefinitionStringConfig,
    CatalogCustomAttributeDefinitionStringConfigDict,
)
from .enums.catalog_custom_attribute_definition_app_visibility import CatalogCustomAttributeDefinitionAppVisibilityOrStr
from .enums.catalog_custom_attribute_definition_seller_visibility import (
    CatalogCustomAttributeDefinitionSellerVisibilityOrStr,
)
from .enums.catalog_custom_attribute_definition_type import CatalogCustomAttributeDefinitionTypeOrStr
from .enums.catalog_object_type import CatalogObjectTypeOrStr
from .source_application import SourceApplication, SourceApplicationDict


class CatalogCustomAttributeDefinition(SdkBaseModel):
    """Contains information defining a custom attribute. Custom attributes are intended to store additional information
    about a catalog object or to associate a catalog object with an entity in another system. Do not use custom
    attributes to store any sensitive information (personally identifiable information, card details, etc.). `Read more
    about custom attributes <https://developer.squareup.com/docs/catalog-api/add-custom-attributes>`__"""

    type_: CatalogCustomAttributeDefinitionTypeOrStr = Field(alias="type")
    """Defines the possible types for a custom attribute."""

    name: str
    """The name of this definition for API and seller-facing UI purposes. The name must be unique within the (merchant,
    application) pair. Required. May not be empty and may not exceed 255 characters. Can be modified after creation."""

    description: OptionalNullable[str] = UNSET
    """Seller-oriented description of the meaning of this Custom Attribute, any constraints that the seller should
    observe, etc. May be displayed as a tooltip in Square UIs."""

    source_application: Optional[SourceApplication] = UNSET
    """Represents information about the application used to generate a change."""

    allowed_object_types: list[CatalogObjectTypeOrStr]
    """The set of ``CatalogObject`` types that this custom atttribute may be applied to. Currently, only ``ITEM``,
    ``ITEM_VARIATION``, ``MODIFIER``, ``MODIFIER_LIST``, and ``CATEGORY`` are allowed. At least one type must be
    included. See `CatalogObjectType <#type-catalogobjecttype>`__ for possible values"""

    seller_visibility: Optional[CatalogCustomAttributeDefinitionSellerVisibilityOrStr] = UNSET
    """Defines the visibility of a custom attribute to sellers in Square client applications, Square APIs or in Square
    UIs (including Square Point of Sale applications and Square Dashboard)."""

    app_visibility: Optional[CatalogCustomAttributeDefinitionAppVisibilityOrStr] = UNSET
    """Defines the visibility of a custom attribute to applications other than their creating application."""

    string_config: Optional[CatalogCustomAttributeDefinitionStringConfig] = UNSET
    """Configuration associated with Custom Attribute Definitions of type ``STRING``."""

    number_config: Optional[CatalogCustomAttributeDefinitionNumberConfig] = UNSET
    selection_config: Optional[CatalogCustomAttributeDefinitionSelectionConfig] = UNSET
    """Configuration associated with ``SELECTION``-type custom attribute definitions."""

    custom_attribute_usage_count: Optional[int] = UNSET
    """The number of custom attributes that reference this custom attribute definition. Set by the server in response to
    a ListCatalog request with ``include_counts`` set to ``true``. If the actual count is greater than 100,
    ``custom_attribute_usage_count`` will be set to ``100``."""

    key: OptionalNullable[str] = UNSET
    """The name of the desired custom attribute key that can be used to access the custom attribute value on catalog
    objects. Cannot be modified after the custom attribute definition has been created. Must be between 1 and 60
    characters, and may only contain the characters ``[a-zA-Z0-9_-]``."""


class CatalogCustomAttributeDefinitionDict(TypedDict):
    type_: CatalogCustomAttributeDefinitionTypeOrStr
    name: str
    description: NotRequired[str | None]
    source_application: NotRequired[SourceApplicationDict]
    allowed_object_types: list[CatalogObjectTypeOrStr]
    seller_visibility: NotRequired[CatalogCustomAttributeDefinitionSellerVisibilityOrStr]
    app_visibility: NotRequired[CatalogCustomAttributeDefinitionAppVisibilityOrStr]
    string_config: NotRequired[CatalogCustomAttributeDefinitionStringConfigDict]
    number_config: NotRequired[CatalogCustomAttributeDefinitionNumberConfigDict]
    selection_config: NotRequired[CatalogCustomAttributeDefinitionSelectionConfigDict]
    custom_attribute_usage_count: NotRequired[int]
    key: NotRequired[str | None]
