from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .catalog_availability_period import CatalogAvailabilityPeriod, CatalogAvailabilityPeriodDict
from .catalog_category import CatalogCategory, CatalogCategoryDict
from .catalog_custom_attribute_definition import CatalogCustomAttributeDefinition, CatalogCustomAttributeDefinitionDict
from .catalog_custom_attribute_value import CatalogCustomAttributeValue, CatalogCustomAttributeValueDict
from .catalog_discount import CatalogDiscount, CatalogDiscountDict
from .catalog_image import CatalogImage, CatalogImageDict
from .catalog_item_option_value import CatalogItemOptionValue, CatalogItemOptionValueDict
from .catalog_item_variation import CatalogItemVariation, CatalogItemVariationDict
from .catalog_measurement_unit import CatalogMeasurementUnit, CatalogMeasurementUnitDict
from .catalog_modifier import CatalogModifier, CatalogModifierDict
from .catalog_pricing_rule import CatalogPricingRule, CatalogPricingRuleDict
from .catalog_product_set import CatalogProductSet, CatalogProductSetDict
from .catalog_quick_amounts_settings import CatalogQuickAmountsSettings, CatalogQuickAmountsSettingsDict
from .catalog_subscription_plan import CatalogSubscriptionPlan, CatalogSubscriptionPlanDict
from .catalog_subscription_plan_variation import CatalogSubscriptionPlanVariation, CatalogSubscriptionPlanVariationDict
from .catalog_tax import CatalogTax, CatalogTaxDict
from .catalog_time_period import CatalogTimePeriod, CatalogTimePeriodDict
from .catalog_v1_id import CatalogV1Id, CatalogV1IdDict
from .enums.catalog_object_type import CatalogObjectTypeOrStr

if TYPE_CHECKING:
    from .catalog_item import CatalogItem, CatalogItemDict
    from .catalog_item_option import CatalogItemOption, CatalogItemOptionDict
    from .catalog_modifier_list import CatalogModifierList, CatalogModifierListDict


class CatalogObject(SdkBaseModel):
    """The wrapper object for the catalog entries of a given object type.

    Depending on the ``type`` attribute value, a ``CatalogObject`` instance assumes a type-specific data to yield the
    corresponding type of catalog object.

    For example, if ``type=ITEM``, the ``CatalogObject`` instance must have the ITEM-specific data set on the
    ``item_data`` attribute. The resulting ``CatalogObject`` instance is also a ``CatalogItem`` instance.

    In general, if ``type=<OBJECT_TYPE>``, the ``CatalogObject`` instance must have the ``<OBJECT_TYPE>``-specific data
    set on the ``<object_type>_data`` attribute. The resulting ``CatalogObject`` instance is also a
    ``Catalog<ObjectType>`` instance.

    For a more detailed discussion of the Catalog data model, please see the `Design a Catalog
    <https://developer.squareup.com/docs/catalog-api/design-a-catalog>`__ guide."""

    type_: CatalogObjectTypeOrStr = Field(alias="type")
    """Possible types of CatalogObjects returned from the catalog, each containing type-specific properties in the
    ``*_data`` field corresponding to the specified object type."""

    id: str
    """An identifier to reference this object in the catalog. When a new ``CatalogObject`` is inserted, the client
    should set the id to a temporary identifier starting with a "``#``" character. Other objects being inserted or
    updated within the same request may use this identifier to refer to the new object.

    When the server receives the new object, it will supply a unique identifier that replaces the temporary identifier
    for all future references."""

    updated_at: Optional[str] = UNSET
    """Last modification `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ in RFC 3339
    format, e.g., ``"2016-08-15T23:59:33.123Z"`` would indicate the UTC time (denoted by ``Z``) of August 15, 2016 at
    23:59:33 and 123 milliseconds."""

    version: Optional[int] = UNSET
    """The version of the object. When updating an object, the version supplied should match the version in the
    database. If it does not, the server attempts a three-way merge. If the client's changes and the concurrent changes
    don't overlap, the merge succeeds silently. A ``VERSION_MISMATCH`` error is only returned when both sides changed
    the same field to different values.

    Use the same API version (``Square-Version`` header) for both reading and writing catalog objects. The server uses
    the API version on a write request to determine which missing fields the client intentionally cleared versus which
    fields the client simply could not see at that version. If a client reads an object at an older API version and
    writes it back at a newer version, fields that were introduced between those two versions will be absent from the
    request, and the server will interpret that absence as an intentional clear."""

    is_deleted: OptionalNullable[bool] = UNSET
    """If ``true``, the object has been deleted from the database. Must be ``false`` for new objects being inserted.
    When deleted, the ``updated_at`` field will equal the deletion time."""

    custom_attribute_values: Optional[dict[str, CatalogCustomAttributeValue | None]] = UNSET
    """A map (key-value pairs) of application-defined custom attribute values. The value of a key-value pair is a
    `CatalogCustomAttributeValue <entity:CatalogCustomAttributeValue>`__ object. The key is the ``key`` attribute value
    defined in the associated `CatalogCustomAttributeDefinition <entity:CatalogCustomAttributeDefinition>`__ object
    defined by the application making the request.

    If the ``CatalogCustomAttributeDefinition`` object is defined by another application, the
    ``CatalogCustomAttributeDefinition``'s key attribute value is prefixed by the defining application ID. For example,
    if the ``CatalogCustomAttributeDefinition`` has a ``key`` attribute of ``"cocoa_brand"`` and the defining
    application ID is ``"abcd1234"``, the key in the map is ``"abcd1234:cocoa_brand"`` if the application making the
    request is different from the application defining the custom attribute definition. Otherwise, the key used in the
    map is simply ``"cocoa_brand"``.

    Application-defined custom attributes are set at a global (location-independent) level. Custom attribute values are
    intended to store additional information about a catalog object or associations with an entity in another system. Do
    not use custom attributes to store any sensitive information (personally identifiable information, card details,
    etc.)."""

    catalog_v1_ids: Optional[list[CatalogV1Id | None]] = UNSET
    """The Connect v1 IDs for this object at each location where it is present, where they differ from the object's
    Connect V2 ID. The field will only be present for objects that have been created or modified by legacy APIs."""

    present_at_all_locations: OptionalNullable[bool] = UNSET
    """Controls whether this object is present at all locations, including future locations.

    Most object types have independent location control, including ``TAX``, ``DISCOUNT``, and ``MODIFIER_LIST``.

    ``ITEM`` and ``ITEM_VARIATION`` have separate settings, but a variation can only be enabled at locations where its
    parent item is enabled. Disabling a variation everywhere is valid even when the parent item is enabled at specific
    locations.

    ``MODIFIER`` objects nested within a ``MODIFIER_LIST`` inherit location settings from their parent. Some object
    types, including ``CATEGORY``, ``IMAGE``, and ``CUSTOM_ATTRIBUTE_DEFINITION``, must always be globally enabled and
    cannot use location-specific fields.

    The field operates in two modes. When true (the default), the object is available at all current and future
    locations except those in ``absent_at_location_ids``. When false, the object is available only at locations in
    ``present_at_location_ids``. The unused list in each mode is ignored."""

    present_at_location_ids: Optional[list[str | None]] = UNSET
    """Locations where the object is present, used when ``present_at_all_locations`` is false.

    When ``present_at_all_locations`` is true, this field is ignored since the object is already present everywhere. Can
    include deactivated locations. Empty strings are rejected."""

    absent_at_location_ids: Optional[list[str | None]] = UNSET
    """Locations where the object is not present, used when ``present_at_all_locations`` is true.

    When ``present_at_all_locations`` is false, this field is ignored since the object is already absent everywhere
    except those in ``present_at_location_ids``. Can include deactivated locations. Empty strings are rejected."""

    item_data: Optional[CatalogItem] = UNSET
    """A `CatalogObject <entity:CatalogObject>`__ instance of the ``ITEM`` type, also referred to as an item, in the
    catalog."""

    category_data: Optional[CatalogCategory] = UNSET
    """A category to which a ``CatalogItem`` instance belongs."""

    item_variation_data: Optional[CatalogItemVariation] = UNSET
    """An item variation, representing a product for sale, in the Catalog object model. Each `item
    <entity:CatalogItem>`__ must have at least one item variation and can have at most 250 item variations.

    An item variation can be sellable, stockable, or both if it has a unit of measure for its count for the sold number
    of the variation, the stocked number of the variation, or both. For example, when a variation representing wine is
    stocked and sold by the bottle, the variation is both stockable and sellable. But when a variation of the wine is
    sold by the glass, the sold units cannot be used as a measure of the stocked units. This by-the-glass variation is
    sellable, but not stockable. To accurately keep track of the wine's inventory count at any time, the sellable count
    must be converted to stockable count. Typically, the seller defines this unit conversion. For example, 1 bottle
    equals 5 glasses. The Square API exposes the ``stockable_conversion`` property on the variation to specify the
    conversion. Thus, when two glasses of the wine are sold, the sellable count decreases by 2, and the stockable count
    automatically decreases by 0.4 bottle according to the conversion."""

    tax_data: Optional[CatalogTax] = UNSET
    """A tax applicable to an item."""

    discount_data: Optional[CatalogDiscount] = UNSET
    """A discount applicable to items."""

    modifier_list_data: Optional[CatalogModifierList] = UNSET
    """A container for a list of modifiers, or a text-based modifier. For text-based modifiers, this represents text
    configuration for an item. (For example, custom text to print on a t-shirt). For non text-based modifiers, this
    represents a list of modifiers that can be applied to items at the time of sale. (For example, a list of condiments
    for a hot dog, or a list of ice cream flavors). Each element of the modifier list is a ``CatalogObject`` instance of
    the ``MODIFIER`` type."""

    modifier_data: Optional[CatalogModifier] = UNSET
    """A modifier that can be applied to items at the time of sale. For example, a cheese modifier for a burger, or a
    flavor modifier for a serving of ice cream."""

    time_period_data: Optional[CatalogTimePeriod] = UNSET
    """Represents a time period - either a single period or a repeating period."""

    product_set_data: Optional[CatalogProductSet] = UNSET
    """Represents a collection of catalog objects for the purpose of applying a ``PricingRule``. Including a catalog
    object will include all of its subtypes. For example, including a category in a product set will include all of its
    items and associated item variations in the product set. Including an item in a product set will also include its
    item variations."""

    pricing_rule_data: Optional[CatalogPricingRule] = UNSET
    """Defines how discounts are automatically applied to a set of items that match the pricing rule during the active
    time period."""

    image_data: Optional[CatalogImage] = UNSET
    """An image file to use in Square catalogs. It can be associated with ``CatalogItem``, ``CatalogItemVariation``,
    ``CatalogCategory``, and ``CatalogModifierList`` objects. Only the images on items and item variations are exposed
    in Dashboard. Only the first image on an item is displayed in Square Point of Sale (SPOS). Images on items and
    variations are displayed through Square Online Store. Images on other object types are for use by 3rd party
    application developers."""

    measurement_unit_data: Optional[CatalogMeasurementUnit] = UNSET
    """Represents the unit used to measure a ``CatalogItemVariation`` and specifies the precision for decimal
    quantities."""

    subscription_plan_data: Optional[CatalogSubscriptionPlan] = UNSET
    """Describes a subscription plan. A subscription plan represents what you want to sell in a subscription model, and
    includes references to each of the associated subscription plan variations. For more information, see `Subscription
    Plans and Variations <https://developer.squareup.com/docs/subscriptions-api/plans-and-variations>`__."""

    item_option_data: Optional[CatalogItemOption] = UNSET
    """A group of variations for a ``CatalogItem``."""

    item_option_value_data: Optional[CatalogItemOptionValue] = UNSET
    """An enumerated value that can link a ``CatalogItemVariation`` to an item option as one of its item option
    values."""

    custom_attribute_definition_data: Optional[CatalogCustomAttributeDefinition] = UNSET
    """Contains information defining a custom attribute. Custom attributes are intended to store additional information
    about a catalog object or to associate a catalog object with an entity in another system. Do not use custom
    attributes to store any sensitive information (personally identifiable information, card details, etc.). `Read more
    about custom attributes <https://developer.squareup.com/docs/catalog-api/add-custom-attributes>`__"""

    quick_amounts_settings_data: Optional[CatalogQuickAmountsSettings] = UNSET
    """A parent Catalog Object model represents a set of Quick Amounts and the settings control the amounts."""

    subscription_plan_variation_data: Optional[CatalogSubscriptionPlanVariation] = UNSET
    """Describes a subscription plan variation. A subscription plan variation represents how the subscription for a
    product or service is sold. For more information, see `Subscription Plans and Variations
    <https://developer.squareup.com/docs/subscriptions-api/plans-and-variations>`__."""

    availability_period_data: Optional[CatalogAvailabilityPeriod] = UNSET
    """Represents a time period of availability."""


class CatalogObjectDict(TypedDict):
    type_: CatalogObjectTypeOrStr
    id: str
    updated_at: NotRequired[str]
    version: NotRequired[int]
    is_deleted: NotRequired[bool | None]
    custom_attribute_values: NotRequired[
        dict[str, CatalogCustomAttributeValue | CatalogCustomAttributeValueDict | None]
    ]
    catalog_v1_ids: NotRequired[list[CatalogV1Id | CatalogV1IdDict | None]]
    present_at_all_locations: NotRequired[bool | None]
    present_at_location_ids: NotRequired[list[str | None]]
    absent_at_location_ids: NotRequired[list[str | None]]
    item_data: NotRequired[CatalogItem | CatalogItemDict]
    category_data: NotRequired[CatalogCategory | CatalogCategoryDict]
    item_variation_data: NotRequired[CatalogItemVariation | CatalogItemVariationDict]
    tax_data: NotRequired[CatalogTax | CatalogTaxDict]
    discount_data: NotRequired[CatalogDiscount | CatalogDiscountDict]
    modifier_list_data: NotRequired[CatalogModifierList | CatalogModifierListDict]
    modifier_data: NotRequired[CatalogModifier | CatalogModifierDict]
    time_period_data: NotRequired[CatalogTimePeriod | CatalogTimePeriodDict]
    product_set_data: NotRequired[CatalogProductSet | CatalogProductSetDict]
    pricing_rule_data: NotRequired[CatalogPricingRule | CatalogPricingRuleDict]
    image_data: NotRequired[CatalogImage | CatalogImageDict]
    measurement_unit_data: NotRequired[CatalogMeasurementUnit | CatalogMeasurementUnitDict]
    subscription_plan_data: NotRequired[CatalogSubscriptionPlan | CatalogSubscriptionPlanDict]
    item_option_data: NotRequired[CatalogItemOption | CatalogItemOptionDict]
    item_option_value_data: NotRequired[CatalogItemOptionValue | CatalogItemOptionValueDict]
    custom_attribute_definition_data: NotRequired[
        CatalogCustomAttributeDefinition | CatalogCustomAttributeDefinitionDict
    ]
    quick_amounts_settings_data: NotRequired[CatalogQuickAmountsSettings | CatalogQuickAmountsSettingsDict]
    subscription_plan_variation_data: NotRequired[
        CatalogSubscriptionPlanVariation | CatalogSubscriptionPlanVariationDict
    ]
    availability_period_data: NotRequired[CatalogAvailabilityPeriod | CatalogAvailabilityPeriodDict]
