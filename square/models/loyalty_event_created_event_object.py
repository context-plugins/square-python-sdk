from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_event import LoyaltyEvent, LoyaltyEventDict


class LoyaltyEventCreatedEventObject(SdkBaseModel):
    loyalty_event: Optional[LoyaltyEvent] = UNSET
    """Provides information about a loyalty event. For more information, see `Search for Balance-Changing Loyalty Events
    <https://developer.squareup.com/docs/loyalty-api/loyalty-events>`__."""


class LoyaltyEventCreatedEventObjectDict(TypedDict):
    loyalty_event: NotRequired[LoyaltyEvent | LoyaltyEventDict]
