from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .catalog_item_option_value_for_item_variation import (
    CatalogItemOptionValueForItemVariation,
    CatalogItemOptionValueForItemVariationDict,
)
from .catalog_item_variation_vendor_information import (
    CatalogItemVariationVendorInformation,
    CatalogItemVariationVendorInformationDict,
)
from .catalog_stock_conversion import CatalogStockConversion, CatalogStockConversionDict
from .enums.catalog_pricing_type import CatalogPricingTypeOrStr
from .enums.inventory_alert_type import InventoryAlertTypeOrStr
from .item_variation_location_overrides import ItemVariationLocationOverrides, ItemVariationLocationOverridesDict
from .money import Money, MoneyDict


class CatalogItemVariation(SdkBaseModel):
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

    item_id: OptionalNullable[str] = UNSET
    """The ID of the ``CatalogItem`` associated with this item variation."""

    name: OptionalNullable[str] = UNSET
    """The item variation's name. This is a searchable attribute for use in applicable query filters.

    Its value has a maximum length of 255 Unicode code points. However, when the parent `item <entity:CatalogItem>`__
    uses `item options <entity:CatalogItemOption>`__, this attribute is auto-generated, read-only, and can be longer
    than 255 Unicode code points."""

    sku: OptionalNullable[str] = UNSET
    """The item variation's SKU, if any. This is a searchable attribute for use in applicable query filters."""

    upc: OptionalNullable[str] = UNSET
    """The universal product code (UPC) of the item variation, if any. This is a searchable attribute for use in
    applicable query filters.

    The value of this attribute should be a number of 12-14 digits long. This restriction is enforced on the Square
    Seller Dashboard, Square Point of Sale or Retail Point of Sale apps, where this attribute shows in the GTIN field.
    If a non-compliant UPC value is assigned to this attribute using the API, the value is not editable on the Seller
    Dashboard, Square Point of Sale or Retail Point of Sale apps unless it is updated to fit the expected format."""

    ordinal: Optional[int] = UNSET
    """The order in which this item variation should be displayed. This value is read-only. On writes, the ordinal for
    each item variation within a parent ``CatalogItem`` is set according to the item variations's position. On reads,
    the value is not guaranteed to be sequential or unique."""

    pricing_type: Optional[CatalogPricingTypeOrStr] = UNSET
    """Indicates whether the price of a CatalogItemVariation should be entered manually at the time of sale."""

    price_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    location_overrides: OptionalNullable[list[ItemVariationLocationOverrides]] = UNSET
    """Per-location price and inventory overrides."""

    track_inventory: OptionalNullable[bool] = UNSET
    """If ``true``, inventory tracking is active for the variation at all locations by default. This value can be
    overridden for specific locations using ``ItemVariationLocationOverrides.track_inventory``. If unset at both levels,
    inventory tracking is disabled."""

    inventory_alert_type: Optional[InventoryAlertTypeOrStr] = UNSET
    """Indicates whether Square should alert the merchant when the inventory quantity of a CatalogItemVariation is
    low."""

    inventory_alert_threshold: OptionalNullable[int] = UNSET
    """If the inventory quantity for the variation is less than or equal to this value and ``inventory_alert_type`` is
    ``LOW_QUANTITY``, the variation displays an alert in the merchant dashboard. This value is always an integer.

    Deprecated because this field has never been global."""

    user_data: OptionalNullable[str] = UNSET
    """Arbitrary user metadata to associate with the item variation. This attribute value length is of Unicode code
    points."""

    service_duration: OptionalNullable[int] = UNSET
    """If the ``CatalogItem`` that owns this item variation is of type ``APPOINTMENTS_SERVICE``, then this is the
    duration of the service in milliseconds. For example, a 30 minute appointment would have the value ``1800000``,
    which is equal to 30 (minutes) * 60 (seconds per minute) * 1000 (milliseconds per second)."""

    available_for_booking: OptionalNullable[bool] = UNSET
    """If the ``CatalogItem`` that owns this item variation is of type ``APPOINTMENTS_SERVICE``, a bool representing
    whether this service is available for booking."""

    item_option_values: OptionalNullable[list[CatalogItemOptionValueForItemVariation]] = UNSET
    """List of item option values associated with this item variation. Listed in the same order as the item options of
    the parent item."""

    measurement_unit_id: OptionalNullable[str] = UNSET
    """ID of the ‘CatalogMeasurementUnit’ that is used to measure the quantity sold of this item variation. If left
    unset, the item will be sold in whole quantities."""

    sellable: OptionalNullable[bool] = UNSET
    """Whether this variation can be sold. The inventory count of a sellable variation indicates the number of units
    available for sale. When a variation is both stockable and sellable, its sellable inventory count can be smaller
    than or equal to its stockable count."""

    stockable: OptionalNullable[bool] = UNSET
    """Whether stock is counted directly on this variation (TRUE) or only on its components (FALSE). When a variation is
    both stockable and sellable, the inventory count of a stockable variation keeps track of the number of units of this
    variation in stock and is not an indicator of the number of units of the variation that can be sold."""

    image_ids: OptionalNullable[list[str]] = UNSET
    """The IDs of images associated with this ``CatalogItemVariation`` instance. These images will be shown to customers
    in Square Online Store."""

    team_member_ids: OptionalNullable[list[str]] = UNSET
    """Tokens of employees that can perform the service represented by this variation. Only valid for variations of type
    ``APPOINTMENTS_SERVICE``."""

    stockable_conversion: Optional[CatalogStockConversion] = UNSET
    """Represents the rule of conversion between a stockable `CatalogItemVariation <entity:CatalogItemVariation>`__ and
    a non-stockable sell-by or receive-by ``CatalogItemVariation`` that share the same underlying stock."""

    kitchen_name: OptionalNullable[str] = UNSET
    """(Optional) Name that the restaurant wants to display to their kitchen workers instead of the customer-facing
    name. e.g., customer name might be "Mega-Jumbo Triplesized" and the kitchen name is "Large container"
    """

    vendor_information: OptionalNullable[list[CatalogItemVariationVendorInformation]] = UNSET
    """Details of the vendor this product is purchased from. This field can be set only if the seller has an active
    subscription to either Square for Retail Premium or Square for Restaurants Premium."""


class CatalogItemVariationDict(TypedDict):
    item_id: NotRequired[str | None]
    name: NotRequired[str | None]
    sku: NotRequired[str | None]
    upc: NotRequired[str | None]
    ordinal: NotRequired[int]
    pricing_type: NotRequired[CatalogPricingTypeOrStr]
    price_money: NotRequired[MoneyDict]
    location_overrides: NotRequired[list[ItemVariationLocationOverridesDict] | None]
    track_inventory: NotRequired[bool | None]
    inventory_alert_type: NotRequired[InventoryAlertTypeOrStr]
    inventory_alert_threshold: NotRequired[int | None]
    user_data: NotRequired[str | None]
    service_duration: NotRequired[int | None]
    available_for_booking: NotRequired[bool | None]
    item_option_values: NotRequired[list[CatalogItemOptionValueForItemVariationDict] | None]
    measurement_unit_id: NotRequired[str | None]
    sellable: NotRequired[bool | None]
    stockable: NotRequired[bool | None]
    image_ids: NotRequired[list[str] | None]
    team_member_ids: NotRequired[list[str] | None]
    stockable_conversion: NotRequired[CatalogStockConversionDict]
    kitchen_name: NotRequired[str | None]
    vendor_information: NotRequired[list[CatalogItemVariationVendorInformationDict] | None]
