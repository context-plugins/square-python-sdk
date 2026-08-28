from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FulfillmentFulfillmentLineItemApplication(str, Enum):
    """The ``line_item_application`` describes what order line items this fulfillment applies to. It can be ``ALL`` or
    ``ENTRY_LIST`` with a supplied list of fulfillment entries."""

    ALL = "ALL"
    """If ``ALL``, ``entries`` must be unset."""

    ENTRY_LIST = "ENTRY_LIST"
    """If ``ENTRY_LIST``, supply a list of ``entries``."""

    __str__ = str.__str__


FulfillmentFulfillmentLineItemApplicationOrStr: TypeAlias = Annotated[
    FulfillmentFulfillmentLineItemApplication | str, open_enum_validator(FulfillmentFulfillmentLineItemApplication)
]
