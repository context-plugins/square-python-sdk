from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MeasurementUnitGeneric(str, Enum):
    UNIT = "UNIT"
    """The generic unit."""

    __str__ = str.__str__


MeasurementUnitGenericOrStr: TypeAlias = Annotated[
    MeasurementUnitGeneric | str, open_enum_validator(MeasurementUnitGeneric)
]
