from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .loyalty_event_accumulate_points import LoyaltyEventAccumulatePoints, LoyaltyEventAccumulatePointsDict


class AccumulateLoyaltyPointsRequest(SdkBaseModel):
    """Represents an `AccumulateLoyaltyPoints <api-endpoint:Loyalty-AccumulateLoyaltyPoints>`__ request."""

    accumulate_points: LoyaltyEventAccumulatePoints
    """Provides metadata when the event ``type`` is ``ACCUMULATE_POINTS``."""

    idempotency_key: str
    """A unique string that identifies the ``AccumulateLoyaltyPoints`` request. Keys can be any valid string but must be
    unique for every request."""

    location_id: str
    """The `location <entity:Location>`__ where the purchase was made."""


class AccumulateLoyaltyPointsRequestDict(TypedDict):
    accumulate_points: LoyaltyEventAccumulatePointsDict
    idempotency_key: str
    location_id: str
