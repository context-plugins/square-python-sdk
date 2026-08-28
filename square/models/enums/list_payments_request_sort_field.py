from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ListPaymentsRequestSortField(str, Enum):
    CREATED_AT = "CREATED_AT"
    OFFLINE_CREATED_AT = "OFFLINE_CREATED_AT"
    UPDATED_AT = "UPDATED_AT"

    __str__ = str.__str__


ListPaymentsRequestSortFieldOrStr: TypeAlias = Annotated[
    ListPaymentsRequestSortField | str, open_enum_validator(ListPaymentsRequestSortField)
]
