from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionEventInfoCode(str, Enum):
    """Supported info codes of a subscription event."""

    LOCATION_NOT_ACTIVE = "LOCATION_NOT_ACTIVE"
    """The location is not active."""

    LOCATION_CANNOT_ACCEPT_PAYMENT = "LOCATION_CANNOT_ACCEPT_PAYMENT"
    """The location cannot accept payments."""

    CUSTOMER_DELETED = "CUSTOMER_DELETED"
    """The subscribing customer profile has been deleted."""

    CUSTOMER_NO_EMAIL = "CUSTOMER_NO_EMAIL"
    """The subscribing customer does not have an email."""

    CUSTOMER_NO_NAME = "CUSTOMER_NO_NAME"
    """The subscribing customer does not have a name."""

    USER_PROVIDED = "USER_PROVIDED"
    """User-provided detail."""

    __str__ = str.__str__


SubscriptionEventInfoCodeOrStr: TypeAlias = Annotated[
    SubscriptionEventInfoCode | str, open_enum_validator(SubscriptionEventInfoCode)
]
