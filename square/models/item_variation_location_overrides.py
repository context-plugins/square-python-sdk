from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.catalog_pricing_type import CatalogPricingTypeOrStr
from .enums.inventory_alert_type import InventoryAlertTypeOrStr
from .money import Money, MoneyDict


class ItemVariationLocationOverrides(SdkBaseModel):
    """Price and inventory alerting overrides for a ``CatalogItemVariation`` at a specific ``Location``."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the ``Location``. This can include locations that are deactivated."""

    price_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    pricing_type: Optional[CatalogPricingTypeOrStr] = UNSET
    """Indicates whether the price of a CatalogItemVariation should be entered manually at the time of sale."""

    track_inventory: OptionalNullable[bool] = UNSET
    """Indicates whether inventory tracking is active for the ``CatalogItemVariation`` at this ``Location``. When set,
    this value explicitly overrides the global ``track_inventory`` setting. When unset, the location should use the
    global value. If both global and location-level values are unset, inventory tracking is disabled."""

    inventory_alert_type: Optional[InventoryAlertTypeOrStr] = UNSET
    """Indicates whether Square should alert the merchant when the inventory quantity of a CatalogItemVariation is
    low."""

    inventory_alert_threshold: OptionalNullable[int] = UNSET
    """If the inventory quantity for the variation is less than or equal to this value and ``inventory_alert_type`` is
    ``LOW_QUANTITY``, the variation displays an alert in the merchant dashboard.

    This value is always an integer."""

    sold_out: Optional[bool] = UNSET
    """Indicates whether the overridden item variation is sold out at the specified location.

    When inventory tracking is enabled on the item variation either globally or at the specified location, the item
    variation is automatically marked as sold out when its inventory count reaches zero. The seller can manually set the
    item variation as sold out even when the inventory count is greater than zero. Attempts by an application to set
    this attribute are ignored. Regardless how the sold-out status is set, applications should treat its inventory count
    as zero when this attribute value is ``true``."""

    sold_out_valid_until: Optional[str] = UNSET
    """The seller-assigned timestamp, of the RFC 3339 format, to indicate when this sold-out variation becomes available
    again at the specified location. Attempts by an application to set this attribute are ignored. When the current time
    is later than this attribute value, the affected item variation is no longer sold out."""


class ItemVariationLocationOverridesDict(TypedDict):
    location_id: NotRequired[str | None]
    price_money: NotRequired[Money | MoneyDict]
    pricing_type: NotRequired[CatalogPricingTypeOrStr]
    track_inventory: NotRequired[bool | None]
    inventory_alert_type: NotRequired[InventoryAlertTypeOrStr]
    inventory_alert_threshold: NotRequired[int | None]
    sold_out: NotRequired[bool]
    sold_out_valid_until: NotRequired[str]
