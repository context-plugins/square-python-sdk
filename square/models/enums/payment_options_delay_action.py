from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PaymentOptionsDelayAction(str, Enum):
    """Describes the action to be applied to a delayed capture payment when the delay_duration has elapsed."""

    CANCEL = "CANCEL"
    """Indicates that the payment should be automatically canceled when the delay duration elapses."""

    COMPLETE = "COMPLETE"
    """Indicates that the payment should be automatically completed when the delay duration elapses."""

    __str__ = str.__str__


PaymentOptionsDelayActionOrStr: TypeAlias = Annotated[
    PaymentOptionsDelayAction | str, open_enum_validator(PaymentOptionsDelayAction)
]
