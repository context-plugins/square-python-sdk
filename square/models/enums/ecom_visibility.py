from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EcomVisibility(str, Enum):
    """Determines item visibility in Ecom (Online Store) and Online Checkout."""

    UNINDEXED = "UNINDEXED"
    """Item is not synced with Ecom (Weebly). This is the default state"""

    UNAVAILABLE = "UNAVAILABLE"
    """Item is synced but is unavailable within Ecom (Weebly) and Online Checkout"""

    HIDDEN = "HIDDEN"
    """Option for seller to choose manually created Quick Amounts."""

    VISIBLE = "VISIBLE"
    """Item is synced but available within Ecom (Weebly) and Online Checkout but is hidden from Ecom Store."""

    __str__ = str.__str__


EcomVisibilityOrStr: TypeAlias = Annotated[EcomVisibility | str, open_enum_validator(EcomVisibility)]
