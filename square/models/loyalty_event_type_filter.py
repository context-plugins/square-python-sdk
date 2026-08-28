from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.loyalty_event_type import LoyaltyEventTypeOrStr


class LoyaltyEventTypeFilter(SdkBaseModel):
    """Filter events by event type."""

    types: list[LoyaltyEventTypeOrStr]
    """The loyalty event types used to filter the result. If multiple values are specified, the endpoint uses a logical
    OR to combine them. See `LoyaltyEventType <#type-loyaltyeventtype>`__ for possible values"""


class LoyaltyEventTypeFilterDict(TypedDict):
    types: list[LoyaltyEventTypeOrStr]
