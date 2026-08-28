from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderCardSurchargeTreatmentType(str, Enum):
    """Indicates whether the card surcharge will be treated as a value-holding line item or apportioned across all line
    items."""

    LINE_ITEM_TREATMENT = "LINE_ITEM_TREATMENT"
    APPORTIONED_TREATMENT = "APPORTIONED_TREATMENT"

    __str__ = str.__str__


OrderCardSurchargeTreatmentTypeOrStr: TypeAlias = Annotated[
    OrderCardSurchargeTreatmentType | str, open_enum_validator(OrderCardSurchargeTreatmentType)
]
