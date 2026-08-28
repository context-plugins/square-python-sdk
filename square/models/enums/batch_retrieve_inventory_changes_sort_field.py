from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BatchRetrieveInventoryChangesSortField(str, Enum):
    OCCURRED_AT = "OCCURRED_AT"

    __str__ = str.__str__


BatchRetrieveInventoryChangesSortFieldOrStr: TypeAlias = Annotated[
    BatchRetrieveInventoryChangesSortField | str, open_enum_validator(BatchRetrieveInventoryChangesSortField)
]
