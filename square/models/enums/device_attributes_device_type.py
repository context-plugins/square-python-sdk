from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DeviceAttributesDeviceType(str, Enum):
    """An enum identifier of the device type."""

    TERMINAL = "TERMINAL"
    HANDHELD = "HANDHELD"

    __str__ = str.__str__


DeviceAttributesDeviceTypeOrStr: TypeAlias = Annotated[
    DeviceAttributesDeviceType | str, open_enum_validator(DeviceAttributesDeviceType)
]
