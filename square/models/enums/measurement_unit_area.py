from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MeasurementUnitArea(str, Enum):
    """Unit of area used to measure a quantity."""

    IMPERIAL_ACRE = "IMPERIAL_ACRE"
    """The area is measured in acres."""

    IMPERIAL_SQUARE_INCH = "IMPERIAL_SQUARE_INCH"
    """The area is measured in square inches."""

    IMPERIAL_SQUARE_FOOT = "IMPERIAL_SQUARE_FOOT"
    """The area is measured in square feet."""

    IMPERIAL_SQUARE_YARD = "IMPERIAL_SQUARE_YARD"
    """The area is measured in square yards."""

    IMPERIAL_SQUARE_MILE = "IMPERIAL_SQUARE_MILE"
    """The area is measured in square miles."""

    METRIC_SQUARE_CENTIMETER = "METRIC_SQUARE_CENTIMETER"
    """The area is measured in square centimeters."""

    METRIC_SQUARE_METER = "METRIC_SQUARE_METER"
    """The area is measured in square meters."""

    METRIC_SQUARE_KILOMETER = "METRIC_SQUARE_KILOMETER"
    """The area is measured in square kilometers."""

    __str__ = str.__str__


MeasurementUnitAreaOrStr: TypeAlias = Annotated[MeasurementUnitArea | str, open_enum_validator(MeasurementUnitArea)]
