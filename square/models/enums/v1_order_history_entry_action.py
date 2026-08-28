from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1OrderHistoryEntryAction(str, Enum):
    ORDER_PLACED = "ORDER_PLACED"
    DECLINED = "DECLINED"
    PAYMENT_RECEIVED = "PAYMENT_RECEIVED"
    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"
    REFUNDED = "REFUNDED"
    EXPIRED = "EXPIRED"

    __str__ = str.__str__


V1OrderHistoryEntryActionOrStr: TypeAlias = Annotated[
    V1OrderHistoryEntryAction | str, open_enum_validator(V1OrderHistoryEntryAction)
]
