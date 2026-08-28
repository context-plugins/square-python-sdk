from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BulkRetrieveChannelsRequestConstants(str, Enum):
    MAX_BATCH_SIZE = "MAX_BATCH_SIZE"

    __str__ = str.__str__


BulkRetrieveChannelsRequestConstantsOrStr: TypeAlias = Annotated[
    BulkRetrieveChannelsRequestConstants | str, open_enum_validator(BulkRetrieveChannelsRequestConstants)
]
