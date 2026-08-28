from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .measurement_unit import MeasurementUnit, MeasurementUnitDict


class OrderQuantityUnit(SdkBaseModel):
    """Contains the measurement unit for a quantity and a precision that specifies the number of digits after the
    decimal point for decimal quantities."""

    measurement_unit: Optional[MeasurementUnit] = UNSET
    """Represents a unit of measurement to use with a quantity, such as ounces or inches. Exactly one of the following
    fields are required: ``custom_unit``, ``area_unit``, ``length_unit``, ``volume_unit``, and ``weight_unit``."""

    precision: OptionalNullable[int] = UNSET
    """For non-integer quantities, represents the number of digits after the decimal point that are recorded for this
    quantity.

    For example, a precision of 1 allows quantities such as ``"1.0"`` and ``"1.1"``, but not ``"1.01"``.

    Min: 0. Max: 5."""

    catalog_object_id: OptionalNullable[str] = UNSET
    """The catalog object ID referencing the `CatalogMeasurementUnit <entity:CatalogMeasurementUnit>`__.

    This field is set when this is a catalog-backed measurement unit."""

    catalog_version: OptionalNullable[int] = UNSET
    """The version of the catalog object that this measurement unit references.

    This field is set when this is a catalog-backed measurement unit."""


class OrderQuantityUnitDict(TypedDict):
    measurement_unit: NotRequired[MeasurementUnit | MeasurementUnitDict]
    precision: NotRequired[int | None]
    catalog_object_id: NotRequired[str | None]
    catalog_version: NotRequired[int | None]
