from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogObjectType(str, Enum):
    """Possible types of CatalogObjects returned from the catalog, each containing type-specific properties in the
    ``*_data`` field corresponding to the specified object type."""

    ITEM = "ITEM"
    """The ``CatalogObject`` instance is of the `CatalogItem <entity:CatalogItem>`__ type and represents an item. The
    item-specific data must be set on the ``item_data`` field."""

    IMAGE = "IMAGE"
    """The ``CatalogObject`` instance is of the `CatalogImage <entity:CatalogImage>`__ type and represents an image. The
    image-specific data must be set on the ``image_data`` field."""

    CATEGORY = "CATEGORY"
    """The ``CatalogObject`` instance is of the `CatalogCategory <entity:CatalogCategory>`__ type and represents a
    category. The category-specific data must be set on the ``category_data`` field."""

    ITEM_VARIATION = "ITEM_VARIATION"
    """The ``CatalogObject`` instance is of the `CatalogItemVariation <entity:CatalogItemVariation>`__ type and
    represents an item variation, also referred to as variation. The item variation-specific data must be set on the
    ``item_variation_data`` field."""

    TAX = "TAX"
    """The ``CatalogObject`` instance is of the `CatalogTax <entity:CatalogTax>`__ type and represents a tax. The
    tax-specific data must be set on the ``tax_data`` field."""

    DISCOUNT = "DISCOUNT"
    """The ``CatalogObject`` instance is of the `CatalogDiscount <entity:CatalogDiscount>`__ type and represents a
    discount. The discount-specific data must be set on the ``discount_data`` field."""

    MODIFIER_LIST = "MODIFIER_LIST"
    """The ``CatalogObject`` instance is of the `CatalogModifierList <entity:CatalogModifierList>`__ type and represents
    a modifier list. The modifier-list-specific data must be set on the ``modifier_list_data`` field."""

    MODIFIER = "MODIFIER"
    """The ``CatalogObject`` instance is of the `CatalogModifier <entity:CatalogModifier>`__ type and represents a
    modifier. The modifier-specific data must be set on the ``modifier_data`` field."""

    PRICING_RULE = "PRICING_RULE"
    """The ``CatalogObject`` instance is of the `CatalogPricingRule <entity:CatalogPricingRule>`__ type and represents a
    pricing rule. The pricing-rule-specific data must be set on the ``pricing_rule_data`` field."""

    PRODUCT_SET = "PRODUCT_SET"
    """The ``CatalogObject`` instance is of the `CatalogProductSet <entity:CatalogProductSet>`__ type and represents a
    product set. The product-set-specific data will be stored in the ``product_set_data`` field."""

    TIME_PERIOD = "TIME_PERIOD"
    """The ``CatalogObject`` instance is of the `CatalogTimePeriod <entity:CatalogTimePeriod>`__ type and represents a
    time period. The time-period-specific data must be set on the ``time_period_data`` field."""

    MEASUREMENT_UNIT = "MEASUREMENT_UNIT"
    """The ``CatalogObject`` instance is of the `CatalogMeasurementUnit <entity:CatalogMeasurementUnit>`__ type and
    represents a measurement unit specifying the unit of measure and precision in which an item variation is sold. The
    measurement-unit-specific data must set on the ``measurement_unit_data`` field."""

    SUBSCRIPTION_PLAN_VARIATION = "SUBSCRIPTION_PLAN_VARIATION"
    """The ``CatalogObject`` instance is of the `CatalogSubscriptionPlan <entity:CatalogSubscriptionPlan>`__ type and
    represents a subscription plan. The subscription-plan-specific data must be stored on the ``subscription_plan_data``
    field."""

    ITEM_OPTION = "ITEM_OPTION"
    """The ``CatalogObject`` instance is of the `CatalogItemOption <entity:CatalogItemOption>`__ type and represents a
    list of options (such as a color or size of a T-shirt) that can be assigned to item variations. The
    item-option-specific data must be on the ``item_option_data`` field."""

    ITEM_OPTION_VAL = "ITEM_OPTION_VAL"
    """The ``CatalogObject`` instance is of the `CatalogItemOptionValue <entity:CatalogItemOptionValue>`__ type and
    represents a value associated with one or more item options. For example, an item option of "Size" may have item
    option values such as "Small" or "Medium". The item-option-value-specific data must be on the
    ``item_option_value_data`` field."""

    CUSTOM_ATTRIBUTE_DEFINITION = "CUSTOM_ATTRIBUTE_DEFINITION"
    """The ``CatalogObject`` instance is of the `CatalogCustomAttributeDefinition
    <entity:CatalogCustomAttributeDefinition>`__ type and represents the definition of a custom attribute. The
    custom-attribute-definition-specific data must be set on the ``custom_attribute_definition_data`` field."""

    QUICK_AMOUNTS_SETTINGS = "QUICK_AMOUNTS_SETTINGS"
    """The ``CatalogObject`` instance is of the `CatalogQuickAmountsSettings <entity:CatalogQuickAmountsSettings>`__
    type and represents settings to configure preset charges for quick payments at each location. For example, a
    location may have a list of both AUTO and MANUAL quick amounts that are set to DISABLED. The
    quick-amounts-settings-specific data must be set on the ``quick_amounts_settings_data`` field."""

    SUBSCRIPTION_PLAN = "SUBSCRIPTION_PLAN"
    """The ``CatalogObject`` instance is of the `CatalogSubscriptionPlan <entity:CatalogSubscriptionPlan>`__ type and
    represents a subscription plan. The subscription plan specific data must be stored on the ``subscription_plan_data``
    field."""

    AVAILABILITY_PERIOD = "AVAILABILITY_PERIOD"
    """The ``CatalogObject`` instance is of the `CatalogAvailabilityPeriod <entity:CatalogAvailabilityPeriod>`__ type
    and represents an availability period. The availability period specific data must be stored on the
    ``availability_period_data`` field."""

    __str__ = str.__str__


CatalogObjectTypeOrStr: TypeAlias = Annotated[CatalogObjectType | str, open_enum_validator(CatalogObjectType)]
