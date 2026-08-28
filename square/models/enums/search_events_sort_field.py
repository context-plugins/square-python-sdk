from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SearchEventsSortField(str, Enum):
    """Specifies the sort key for events returned from a search."""

    DEFAULT = "DEFAULT"
    """Use the default sort key. The default behavior is to sort events by when they were created (``created_at``)."""

    __str__ = str.__str__


SearchEventsSortFieldOrStr: TypeAlias = Annotated[
    SearchEventsSortField | str, open_enum_validator(SearchEventsSortField)
]
