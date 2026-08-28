from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .loyalty_event import LoyaltyEvent, LoyaltyEventDict


class AccumulateLoyaltyPointsResponse(SdkBaseModel):
    """Represents an `AccumulateLoyaltyPoints <api-endpoint:Loyalty-AccumulateLoyaltyPoints>`__ response."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    event: Optional[LoyaltyEvent] = UNSET
    """Provides information about a loyalty event. For more information, see `Search for Balance-Changing Loyalty Events
    <https://developer.squareup.com/docs/loyalty-api/loyalty-events>`__."""

    events: Optional[list[LoyaltyEvent]] = UNSET
    """The resulting loyalty events. If the purchase qualifies for points, the ``ACCUMULATE_POINTS`` event is always
    included. When using the Orders API, the ``ACCUMULATE_PROMOTION_POINTS`` event is included if the purchase also
    qualifies for a loyalty promotion."""


class AccumulateLoyaltyPointsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    event: NotRequired[LoyaltyEvent | LoyaltyEventDict]
    events: NotRequired[list[LoyaltyEvent | LoyaltyEventDict]]
