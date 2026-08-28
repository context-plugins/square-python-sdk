from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VendorUpdatedEventObjectOperation(str, Enum):
    """The operation that can be performed against a vendor to cause the event to be published."""

    UPDATED = "UPDATED"

    __str__ = str.__str__


VendorUpdatedEventObjectOperationOrStr: TypeAlias = Annotated[
    VendorUpdatedEventObjectOperation | str, open_enum_validator(VendorUpdatedEventObjectOperation)
]
