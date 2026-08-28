from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GiftCardStatus(str, Enum):
    """Indicates the gift card state."""

    ACTIVE = "ACTIVE"
    """The gift card is active and can be used as a payment source."""

    DEACTIVATED = "DEACTIVATED"
    """Any activity that changes the gift card balance is permanently forbidden."""

    BLOCKED = "BLOCKED"
    """Any activity that changes the gift card balance is temporarily forbidden."""

    PENDING = "PENDING"
    """The gift card is pending activation. This is the initial state when a gift card is created. Typically, you'll
    call `CreateGiftCardActivity <api-endpoint:GiftCardActivities-CreateGiftCardActivity>`__ to create an ``ACTIVATE``
    activity that activates the gift card with an initial balance before first use."""

    __str__ = str.__str__


GiftCardStatusOrStr: TypeAlias = Annotated[GiftCardStatus | str, open_enum_validator(GiftCardStatus)]
