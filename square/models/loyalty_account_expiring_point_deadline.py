from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LoyaltyAccountExpiringPointDeadline(SdkBaseModel):
    """Represents a set of points for a loyalty account that are scheduled to expire on a specific date."""

    points: int
    """The number of points scheduled to expire at the ``expires_at`` timestamp."""

    expires_at: str
    """The timestamp of when the points are scheduled to expire, in RFC 3339 format."""


class LoyaltyAccountExpiringPointDeadlineDict(TypedDict):
    points: int
    expires_at: str
