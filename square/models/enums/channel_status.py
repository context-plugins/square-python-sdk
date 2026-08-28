from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChannelStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    __str__ = str.__str__


ChannelStatusOrStr: TypeAlias = Annotated[ChannelStatus | str, open_enum_validator(ChannelStatus)]
