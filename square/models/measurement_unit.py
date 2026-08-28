from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.measurement_unit_area import MeasurementUnitAreaOrStr
from .enums.measurement_unit_generic import MeasurementUnitGenericOrStr
from .enums.measurement_unit_length import MeasurementUnitLengthOrStr
from .enums.measurement_unit_time import MeasurementUnitTimeOrStr
from .enums.measurement_unit_unit_type import MeasurementUnitUnitTypeOrStr
from .enums.measurement_unit_volume import MeasurementUnitVolumeOrStr
from .enums.measurement_unit_weight import MeasurementUnitWeightOrStr
from .measurement_unit_custom import MeasurementUnitCustom, MeasurementUnitCustomDict


class MeasurementUnit(SdkBaseModel):
    """Represents a unit of measurement to use with a quantity, such as ounces or inches. Exactly one of the following
    fields are required: ``custom_unit``, ``area_unit``, ``length_unit``, ``volume_unit``, and ``weight_unit``."""

    custom_unit: Optional[MeasurementUnitCustom] = UNSET
    """The information needed to define a custom unit, provided by the seller."""

    area_unit: Optional[MeasurementUnitAreaOrStr] = UNSET
    """Unit of area used to measure a quantity."""

    length_unit: Optional[MeasurementUnitLengthOrStr] = UNSET
    """The unit of length used to measure a quantity."""

    volume_unit: Optional[MeasurementUnitVolumeOrStr] = UNSET
    """The unit of volume used to measure a quantity."""

    weight_unit: Optional[MeasurementUnitWeightOrStr] = UNSET
    """Unit of weight used to measure a quantity."""

    generic_unit: Optional[MeasurementUnitGenericOrStr] = UNSET
    time_unit: Optional[MeasurementUnitTimeOrStr] = UNSET
    """Unit of time used to measure a quantity (a duration)."""

    type_: Optional[MeasurementUnitUnitTypeOrStr] = Field(default=UNSET, alias="type")
    """Describes the type of this unit and indicates which field contains the unit information. This is an ‘open’
    enum."""


class MeasurementUnitDict(TypedDict):
    custom_unit: NotRequired[MeasurementUnitCustom | MeasurementUnitCustomDict]
    area_unit: NotRequired[MeasurementUnitAreaOrStr]
    length_unit: NotRequired[MeasurementUnitLengthOrStr]
    volume_unit: NotRequired[MeasurementUnitVolumeOrStr]
    weight_unit: NotRequired[MeasurementUnitWeightOrStr]
    generic_unit: NotRequired[MeasurementUnitGenericOrStr]
    time_unit: NotRequired[MeasurementUnitTimeOrStr]
    type_: NotRequired[MeasurementUnitUnitTypeOrStr]
