from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .gift_card_activity import GiftCardActivity, GiftCardActivityDict


class CreateGiftCardActivityResponse(SdkBaseModel):
    """A response that contains a ``GiftCardActivity`` that was created. The response might contain a set of ``Error``
    objects if the request resulted in errors."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    gift_card_activity: Optional[GiftCardActivity] = UNSET
    """Represents an action performed on a `gift card <entity:GiftCard>`__ that affects its state or balance. A gift
    card activity contains information about a specific activity type. For example, a ``REDEEM`` activity includes a
    ``redeem_activity_details`` field that contains information about the redemption."""


class CreateGiftCardActivityResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    gift_card_activity: NotRequired[GiftCardActivityDict]
