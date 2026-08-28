from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ListPaymentRefundsRequestSortField(str, Enum):
    CREATED_AT = "CREATED_AT"
    UPDATED_AT = "UPDATED_AT"

    __str__ = str.__str__


ListPaymentRefundsRequestSortFieldOrStr: TypeAlias = Annotated[
    ListPaymentRefundsRequestSortField | str, open_enum_validator(ListPaymentRefundsRequestSortField)
]
