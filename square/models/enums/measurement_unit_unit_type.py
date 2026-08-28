from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MeasurementUnitUnitType(str, Enum):
    """Describes the type of this unit and indicates which field contains the unit information. This is an ‘open’
    enum."""

    TYPE_CUSTOM = "TYPE_CUSTOM"
    """The unit details are contained in the custom_unit field."""

    TYPE_AREA = "TYPE_AREA"
    """The unit details are contained in the area_unit field."""

    TYPE_LENGTH = "TYPE_LENGTH"
    """The unit details are contained in the length_unit field."""

    TYPE_VOLUME = "TYPE_VOLUME"
    """The unit details are contained in the volume_unit field."""

    TYPE_WEIGHT = "TYPE_WEIGHT"
    """The unit details are contained in the weight_unit field."""

    TYPE_GENERIC = "TYPE_GENERIC"
    """The unit details are contained in the generic_unit field."""

    __str__ = str.__str__


MeasurementUnitUnitTypeOrStr: TypeAlias = Annotated[
    MeasurementUnitUnitType | str, open_enum_validator(MeasurementUnitUnitType)
]
