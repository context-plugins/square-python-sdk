from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_event_filter import LoyaltyEventFilter, LoyaltyEventFilterDict


class LoyaltyEventQuery(SdkBaseModel):
    """Represents a query used to search for loyalty events."""

    filter: Optional[LoyaltyEventFilter] = UNSET
    """The filtering criteria. If the request specifies multiple filters, the endpoint uses a logical AND to evaluate
    them."""


class LoyaltyEventQueryDict(TypedDict):
    filter: NotRequired[LoyaltyEventFilterDict]
