from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SearchOrdersSortField(str, Enum):
    """Specifies which timestamp to use to sort ``SearchOrder`` results."""

    CREATED_AT = "CREATED_AT"
    """The time when the order was created, in RFC-3339 format. If you are also filtering for a time range in this
    query, you must set the ``CREATED_AT`` field in your ``DateTimeFilter``."""

    UPDATED_AT = "UPDATED_AT"
    """The time when the order last updated, in RFC-3339 format. If you are also filtering for a time range in this
    query, you must set the ``UPDATED_AT`` field in your ``DateTimeFilter``."""

    CLOSED_AT = "CLOSED_AT"
    """The time when the order was closed, in RFC-3339 format. If you use this value, you must also set a
    ``StateFilter`` with closed states. If you are also filtering for a time range in this query, you must set the
    ``CLOSED_AT`` field in your ``DateTimeFilter``."""

    __str__ = str.__str__


SearchOrdersSortFieldOrStr: TypeAlias = Annotated[
    SearchOrdersSortField | str, open_enum_validator(SearchOrdersSortField)
]
