from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .measurement_unit import MeasurementUnit, MeasurementUnitDict


class StandardUnitDescription(SdkBaseModel):
    """Contains the name and abbreviation for standard measurement unit."""

    unit: Optional[MeasurementUnit] = UNSET
    """Represents a unit of measurement to use with a quantity, such as ounces or inches. Exactly one of the following
    fields are required: ``custom_unit``, ``area_unit``, ``length_unit``, ``volume_unit``, and ``weight_unit``."""

    name: OptionalNullable[str] = UNSET
    """UI display name of the measurement unit. For example, 'Pound'."""

    abbreviation: OptionalNullable[str] = UNSET
    """UI display abbreviation for the measurement unit. For example, 'lb'."""


class StandardUnitDescriptionDict(TypedDict):
    unit: NotRequired[MeasurementUnit | MeasurementUnitDict]
    name: NotRequired[str | None]
    abbreviation: NotRequired[str | None]
