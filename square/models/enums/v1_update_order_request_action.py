from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1UpdateOrderRequestAction(str, Enum):
    COMPLETE = "COMPLETE"
    CANCEL = "CANCEL"
    REFUND = "REFUND"

    __str__ = str.__str__


V1UpdateOrderRequestActionOrStr: TypeAlias = Annotated[
    V1UpdateOrderRequestAction | str, open_enum_validator(V1UpdateOrderRequestAction)
]
