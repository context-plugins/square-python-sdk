from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogQuickAmountType(str, Enum):
    """Determines the type of a specific Quick Amount."""

    QUICK_AMOUNT_TYPE_MANUAL = "QUICK_AMOUNT_TYPE_MANUAL"
    """Quick Amount is created manually by the seller."""

    QUICK_AMOUNT_TYPE_AUTO = "QUICK_AMOUNT_TYPE_AUTO"
    """Quick Amount is generated automatically by machine learning algorithms."""

    __str__ = str.__str__


CatalogQuickAmountTypeOrStr: TypeAlias = Annotated[
    CatalogQuickAmountType | str, open_enum_validator(CatalogQuickAmountType)
]
