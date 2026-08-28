from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DeviceCodeStatus(str, Enum):
    """DeviceCode.Status enum."""

    UNKNOWN = "UNKNOWN"
    """The status cannot be determined or does not exist."""

    UNPAIRED = "UNPAIRED"
    """The device code is just created and unpaired."""

    PAIRED = "PAIRED"
    """The device code has been signed in and paired to a device."""

    EXPIRED = "EXPIRED"
    """The device code was unpaired and expired before it was paired."""

    __str__ = str.__str__


DeviceCodeStatusOrStr: TypeAlias = Annotated[DeviceCodeStatus | str, open_enum_validator(DeviceCodeStatus)]
