from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class CalculateLoyaltyPointsResponse(SdkBaseModel):
    """Represents a `CalculateLoyaltyPoints <api-endpoint:Loyalty-CalculateLoyaltyPoints>`__ response."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    points: Optional[int] = UNSET
    """The number of points that the buyer can earn from the base loyalty program."""

    promotion_points: Optional[int] = UNSET
    """The number of points that the buyer can earn from a loyalty promotion. To be eligible to earn promotion points,
    the purchase must first qualify for program points. When ``order_id`` is not provided in the request, this value is
    always 0."""


class CalculateLoyaltyPointsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    points: NotRequired[int]
    promotion_points: NotRequired[int]
