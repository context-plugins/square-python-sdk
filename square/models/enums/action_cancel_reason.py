from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ActionCancelReason(str, Enum):
    BUYER_CANCELED = "BUYER_CANCELED"
    """A person canceled the ``TerminalCheckout`` from a Square device."""

    SELLER_CANCELED = "SELLER_CANCELED"
    """A client canceled the ``TerminalCheckout`` using the API."""

    TIMED_OUT = "TIMED_OUT"
    """The ``TerminalCheckout`` timed out (see ``deadline_duration`` on the ``TerminalCheckout``)."""

    __str__ = str.__str__


ActionCancelReasonOrStr: TypeAlias = Annotated[ActionCancelReason | str, open_enum_validator(ActionCancelReason)]
