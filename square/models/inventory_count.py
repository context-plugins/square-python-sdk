from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.inventory_state import InventoryStateOrStr


class InventoryCount(SdkBaseModel):
    """Represents Square-estimated quantity of items in a particular state at a particular seller location based on the
    known history of physical counts and inventory adjustments. The absence of an inventory count indicates that the
    catalog object hasn't interacted with the given inventory state at the given location."""

    catalog_object_id: OptionalNullable[str] = UNSET
    """The Square-generated ID of the `CatalogObject <entity:CatalogObject>`__ being tracked."""

    catalog_object_type: OptionalNullable[str] = UNSET
    """The `type <entity:CatalogObjectType>`__ of the `CatalogObject <entity:CatalogObject>`__ being tracked.

    The Inventory API supports setting and reading the ``"catalog_object_type": "ITEM_VARIATION"`` field value. In
    addition, it can also read the ``"catalog_object_type": "ITEM"`` field value that is set by the Square Restaurants
    app."""

    state: Optional[InventoryStateOrStr] = UNSET
    """Indicates the state of a tracked item quantity in the lifecycle of goods."""

    location_id: OptionalNullable[str] = UNSET
    """The Square-generated ID of the `Location <entity:Location>`__ where the related quantity of items is being
    tracked."""

    quantity: OptionalNullable[str] = UNSET
    """The number of items affected by the estimated count as a decimal string. Can support up to 5 digits after the
    decimal point."""

    calculated_at: Optional[str] = UNSET
    """An RFC 3339-formatted timestamp that indicates when the most recent physical count or adjustment affecting the
    estimated count is received."""

    is_estimated: Optional[bool] = UNSET
    """Whether the inventory count is for composed variation (TRUE) or not (FALSE). If true, the inventory count will
    not be present in the response of any of these endpoints: `BatchChangeInventory
    <api-endpoint:Inventory-BatchChangeInventory>`__, `BatchRetrieveInventoryChanges
    <api-endpoint:Inventory-BatchRetrieveInventoryChanges>`__, `BatchRetrieveInventoryCounts
    <api-endpoint:Inventory-BatchRetrieveInventoryCounts>`__, and `RetrieveInventoryChanges
    <api-endpoint:Inventory-RetrieveInventoryChanges>`__."""


class InventoryCountDict(TypedDict):
    catalog_object_id: NotRequired[str | None]
    catalog_object_type: NotRequired[str | None]
    state: NotRequired[InventoryStateOrStr]
    location_id: NotRequired[str | None]
    quantity: NotRequired[str | None]
    calculated_at: NotRequired[str]
    is_estimated: NotRequired[bool]
