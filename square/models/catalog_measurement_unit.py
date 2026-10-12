from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .measurement_unit import MeasurementUnit, MeasurementUnitDict


class CatalogMeasurementUnit(SdkBaseModel):
    """Represents the unit used to measure a ``CatalogItemVariation`` and specifies the precision for decimal
    quantities."""

    measurement_unit: Optional[MeasurementUnit] = UNSET
    """Represents a unit of measurement to use with a quantity, such as ounces or inches. Exactly one of the following
    fields are required: ``custom_unit``, ``area_unit``, ``length_unit``, ``volume_unit``, and ``weight_unit``."""

    precision: OptionalNullable[int] = UNSET
    """An integer between 0 and 5 that represents the maximum number of positions allowed after the decimal in
    quantities measured with this unit. For example:

    - if the precision is 0, the quantity can be 1, 2, 3, etc.
    - if the precision is 1, the quantity can be 0.1, 0.2, etc.
    - if the precision is 2, the quantity can be 0.01, 0.12, etc.

    Default: 3"""


class CatalogMeasurementUnitDict(TypedDict):
    measurement_unit: NotRequired[MeasurementUnitDict]
    precision: NotRequired[int | None]
