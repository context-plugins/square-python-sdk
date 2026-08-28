from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .loyalty_event import LoyaltyEvent, LoyaltyEventDict


class AdjustLoyaltyPointsResponse(SdkBaseModel):
    """Represents an `AdjustLoyaltyPoints <api-endpoint:Loyalty-AdjustLoyaltyPoints>`__ request."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    event: Optional[LoyaltyEvent] = UNSET
    """Provides information about a loyalty event. For more information, see `Search for Balance-Changing Loyalty Events
    <https://developer.squareup.com/docs/loyalty-api/loyalty-events>`__."""


class AdjustLoyaltyPointsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    event: NotRequired[LoyaltyEvent | LoyaltyEventDict]
