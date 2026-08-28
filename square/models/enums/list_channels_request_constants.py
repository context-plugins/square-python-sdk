from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ListChannelsRequestConstants(str, Enum):
    MAX_PAGE_SIZE = "MAX_PAGE_SIZE"

    __str__ = str.__str__


ListChannelsRequestConstantsOrStr: TypeAlias = Annotated[
    ListChannelsRequestConstants | str, open_enum_validator(ListChannelsRequestConstants)
]
