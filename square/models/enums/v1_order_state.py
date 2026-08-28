from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1OrderState(str, Enum):
    PENDING = "PENDING"
    OPEN = "OPEN"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"
    REFUNDED = "REFUNDED"
    REJECTED = "REJECTED"

    __str__ = str.__str__


V1OrderStateOrStr: TypeAlias = Annotated[V1OrderState | str, open_enum_validator(V1OrderState)]
