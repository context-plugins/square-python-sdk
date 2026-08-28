from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SearchVendorsRequestSortField(str, Enum):
    """The field to sort the returned `Vendor <entity:Vendor>`__ objects by."""

    NAME = "NAME"
    """To sort the result by the name of the `Vendor <entity:Vendor>`__ objects."""

    CREATED_AT = "CREATED_AT"
    """To sort the result by the creation time of the `Vendor <entity:Vendor>`__ objects."""

    __str__ = str.__str__


SearchVendorsRequestSortFieldOrStr: TypeAlias = Annotated[
    SearchVendorsRequestSortField | str, open_enum_validator(SearchVendorsRequestSortField)
]
