from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MerchantStatus(str, Enum):
    ACTIVE = "ACTIVE"
    """A fully operational merchant account. The merchant can interact with Square products and APIs."""

    INACTIVE = "INACTIVE"
    """A functionally limited merchant account. The merchant can only have limited interaction via Square APIs. The
    merchant cannot log in or access the seller dashboard."""

    __str__ = str.__str__


MerchantStatusOrStr: TypeAlias = Annotated[MerchantStatus | str, open_enum_validator(MerchantStatus)]
