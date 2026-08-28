from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MeasurementUnitVolume(str, Enum):
    """The unit of volume used to measure a quantity."""

    GENERIC_FLUID_OUNCE = "GENERIC_FLUID_OUNCE"
    """The volume is measured in ounces."""

    GENERIC_SHOT = "GENERIC_SHOT"
    """The volume is measured in shots."""

    GENERIC_CUP = "GENERIC_CUP"
    """The volume is measured in cups."""

    GENERIC_PINT = "GENERIC_PINT"
    """The volume is measured in pints."""

    GENERIC_QUART = "GENERIC_QUART"
    """The volume is measured in quarts."""

    GENERIC_GALLON = "GENERIC_GALLON"
    """The volume is measured in gallons."""

    IMPERIAL_CUBIC_INCH = "IMPERIAL_CUBIC_INCH"
    """The volume is measured in cubic inches."""

    IMPERIAL_CUBIC_FOOT = "IMPERIAL_CUBIC_FOOT"
    """The volume is measured in cubic feet."""

    IMPERIAL_CUBIC_YARD = "IMPERIAL_CUBIC_YARD"
    """The volume is measured in cubic yards."""

    METRIC_MILLILITER = "METRIC_MILLILITER"
    """The volume is measured in metric milliliters."""

    METRIC_LITER = "METRIC_LITER"
    """The volume is measured in metric liters."""

    __str__ = str.__str__


MeasurementUnitVolumeOrStr: TypeAlias = Annotated[
    MeasurementUnitVolume | str, open_enum_validator(MeasurementUnitVolume)
]
