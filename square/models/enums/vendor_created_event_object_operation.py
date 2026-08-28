from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VendorCreatedEventObjectOperation(str, Enum):
    """The operation that can be performed against a vendor to cause the event to be published."""

    CREATED = "CREATED"

    __str__ = str.__str__


VendorCreatedEventObjectOperationOrStr: TypeAlias = Annotated[
    VendorCreatedEventObjectOperation | str, open_enum_validator(VendorCreatedEventObjectOperation)
]
