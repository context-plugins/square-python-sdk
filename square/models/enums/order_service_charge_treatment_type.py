from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderServiceChargeTreatmentType(str, Enum):
    """Indicates whether the service charge will be treated as a value-holding line item or apportioned toward a line
    item."""

    LINE_ITEM_TREATMENT = "LINE_ITEM_TREATMENT"
    APPORTIONED_TREATMENT = "APPORTIONED_TREATMENT"

    __str__ = str.__str__


OrderServiceChargeTreatmentTypeOrStr: TypeAlias = Annotated[
    OrderServiceChargeTreatmentType | str, open_enum_validator(OrderServiceChargeTreatmentType)
]
