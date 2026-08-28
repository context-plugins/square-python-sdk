from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CustomerSortField(str, Enum):
    """Specifies customer attributes as the sort key to customer profiles returned from a search."""

    DEFAULT = "DEFAULT"
    """Use the default sort key. By default, customers are sorted alphanumerically by concatenating their ``given_name``
    and ``family_name``. If neither name field is set, string comparison is performed using one of the remaining fields
    in the following order: ``company_name``, ``email``, ``phone_number``."""

    CREATED_AT = "CREATED_AT"
    """Use the creation date attribute (``created_at``) of customer profiles as the sort key."""

    __str__ = str.__str__


CustomerSortFieldOrStr: TypeAlias = Annotated[CustomerSortField | str, open_enum_validator(CustomerSortField)]
