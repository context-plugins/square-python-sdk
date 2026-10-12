from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_event_date_time_filter import LoyaltyEventDateTimeFilter, LoyaltyEventDateTimeFilterDict
from .loyalty_event_location_filter import LoyaltyEventLocationFilter, LoyaltyEventLocationFilterDict
from .loyalty_event_loyalty_account_filter import LoyaltyEventLoyaltyAccountFilter, LoyaltyEventLoyaltyAccountFilterDict
from .loyalty_event_order_filter import LoyaltyEventOrderFilter, LoyaltyEventOrderFilterDict
from .loyalty_event_type_filter import LoyaltyEventTypeFilter, LoyaltyEventTypeFilterDict


class LoyaltyEventFilter(SdkBaseModel):
    """The filtering criteria. If the request specifies multiple filters, the endpoint uses a logical AND to evaluate
    them."""

    loyalty_account_filter: Optional[LoyaltyEventLoyaltyAccountFilter] = UNSET
    """Filter events by loyalty account."""

    type_filter: Optional[LoyaltyEventTypeFilter] = UNSET
    """Filter events by event type."""

    date_time_filter: Optional[LoyaltyEventDateTimeFilter] = UNSET
    """Filter events by date time range."""

    location_filter: Optional[LoyaltyEventLocationFilter] = UNSET
    """Filter events by location."""

    order_filter: Optional[LoyaltyEventOrderFilter] = UNSET
    """Filter events by the order associated with the event."""


class LoyaltyEventFilterDict(TypedDict):
    loyalty_account_filter: NotRequired[LoyaltyEventLoyaltyAccountFilterDict]
    type_filter: NotRequired[LoyaltyEventTypeFilterDict]
    date_time_filter: NotRequired[LoyaltyEventDateTimeFilterDict]
    location_filter: NotRequired[LoyaltyEventLocationFilterDict]
    order_filter: NotRequired[LoyaltyEventOrderFilterDict]
