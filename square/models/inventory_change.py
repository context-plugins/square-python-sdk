from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_measurement_unit import CatalogMeasurementUnit, CatalogMeasurementUnitDict
from .enums.inventory_change_type import InventoryChangeTypeOrStr
from .inventory_adjustment import InventoryAdjustment, InventoryAdjustmentDict
from .inventory_physical_count import InventoryPhysicalCount, InventoryPhysicalCountDict


class InventoryChange(SdkBaseModel):
    """Represents a single physical count, inventory, adjustment, or transfer that is part of the history of inventory
    changes for a particular `CatalogObject <entity:CatalogObject>`__ instance."""

    type_: Optional[InventoryChangeTypeOrStr] = Field(default=UNSET, alias="type")
    """Indicates how the inventory change was applied to a tracked product quantity."""

    physical_count: Optional[InventoryPhysicalCount] = UNSET
    """Represents the quantity of an item variation that is physically present at a specific location, verified by a
    seller or a seller's employee. For example, a physical count might come from an employee counting the item
    variations on hand or from syncing with an external system."""

    adjustment: Optional[InventoryAdjustment] = UNSET
    """Represents a change in state or quantity of product inventory at a particular time and location."""

    measurement_unit: Optional[CatalogMeasurementUnit] = UNSET
    """Represents the unit used to measure a ``CatalogItemVariation`` and specifies the precision for decimal
    quantities."""

    measurement_unit_id: Optional[str] = UNSET
    """The ID of the `CatalogMeasurementUnit <entity:CatalogMeasurementUnit>`__ object representing the catalog
    measurement unit associated with the inventory change."""


class InventoryChangeDict(TypedDict):
    type_: NotRequired[InventoryChangeTypeOrStr]
    physical_count: NotRequired[InventoryPhysicalCount | InventoryPhysicalCountDict]
    adjustment: NotRequired[InventoryAdjustment | InventoryAdjustmentDict]
    measurement_unit: NotRequired[CatalogMeasurementUnit | CatalogMeasurementUnitDict]
    measurement_unit_id: NotRequired[str]
