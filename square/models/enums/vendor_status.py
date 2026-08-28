from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VendorStatus(str, Enum):
    """The status of the `Vendor <entity:Vendor>`__, whether a `Vendor <entity:Vendor>`__ is active or inactive."""

    ACTIVE = "ACTIVE"
    """Vendor is active and can receive purchase orders."""

    INACTIVE = "INACTIVE"
    """Vendor is inactive and cannot receive purchase orders."""

    __str__ = str.__str__


VendorStatusOrStr: TypeAlias = Annotated[VendorStatus | str, open_enum_validator(VendorStatus)]
