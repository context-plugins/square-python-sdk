from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MeasurementUnitWeight(str, Enum):
    """Unit of weight used to measure a quantity."""

    IMPERIAL_WEIGHT_OUNCE = "IMPERIAL_WEIGHT_OUNCE"
    """The weight is measured in ounces."""

    IMPERIAL_POUND = "IMPERIAL_POUND"
    """The weight is measured in pounds."""

    IMPERIAL_STONE = "IMPERIAL_STONE"
    """The weight is measured in stones."""

    METRIC_MILLIGRAM = "METRIC_MILLIGRAM"
    """The weight is measured in milligrams."""

    METRIC_GRAM = "METRIC_GRAM"
    """The weight is measured in grams."""

    METRIC_KILOGRAM = "METRIC_KILOGRAM"
    """The weight is measured in kilograms."""

    __str__ = str.__str__


MeasurementUnitWeightOrStr: TypeAlias = Annotated[
    MeasurementUnitWeight | str, open_enum_validator(MeasurementUnitWeight)
]
