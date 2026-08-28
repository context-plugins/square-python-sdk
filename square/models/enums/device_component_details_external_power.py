from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DeviceComponentDetailsExternalPower(str, Enum):
    """An enum for ExternalPower."""

    AVAILABLE_CHARGING = "AVAILABLE_CHARGING"
    """Plugged in and charging."""

    AVAILABLE_NOT_IN_USE = "AVAILABLE_NOT_IN_USE"
    """Fully charged."""

    UNAVAILABLE = "UNAVAILABLE"
    """On battery power."""

    AVAILABLE_INSUFFICIENT = "AVAILABLE_INSUFFICIENT"
    """Not providing enough power for the device."""

    __str__ = str.__str__


DeviceComponentDetailsExternalPowerOrStr: TypeAlias = Annotated[
    DeviceComponentDetailsExternalPower | str, open_enum_validator(DeviceComponentDetailsExternalPower)
]
