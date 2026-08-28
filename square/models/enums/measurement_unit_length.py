from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MeasurementUnitLength(str, Enum):
    """The unit of length used to measure a quantity."""

    IMPERIAL_INCH = "IMPERIAL_INCH"
    """The length is measured in inches."""

    IMPERIAL_FOOT = "IMPERIAL_FOOT"
    """The length is measured in feet."""

    IMPERIAL_YARD = "IMPERIAL_YARD"
    """The length is measured in yards."""

    IMPERIAL_MILE = "IMPERIAL_MILE"
    """The length is measured in miles."""

    METRIC_MILLIMETER = "METRIC_MILLIMETER"
    """The length is measured in millimeters."""

    METRIC_CENTIMETER = "METRIC_CENTIMETER"
    """The length is measured in centimeters."""

    METRIC_METER = "METRIC_METER"
    """The length is measured in meters."""

    METRIC_KILOMETER = "METRIC_KILOMETER"
    """The length is measured in kilometers."""

    __str__ = str.__str__


MeasurementUnitLengthOrStr: TypeAlias = Annotated[
    MeasurementUnitLength | str, open_enum_validator(MeasurementUnitLength)
]
