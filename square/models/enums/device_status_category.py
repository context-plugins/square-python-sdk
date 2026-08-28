from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DeviceStatusCategory(str, Enum):
    AVAILABLE = "AVAILABLE"
    NEEDS_ATTENTION = "NEEDS_ATTENTION"
    OFFLINE = "OFFLINE"

    __str__ = str.__str__


DeviceStatusCategoryOrStr: TypeAlias = Annotated[DeviceStatusCategory | str, open_enum_validator(DeviceStatusCategory)]
