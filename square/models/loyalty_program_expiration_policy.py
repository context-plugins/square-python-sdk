from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LoyaltyProgramExpirationPolicy(SdkBaseModel):
    """Describes when the loyalty program expires."""

    expiration_duration: str
    """The number of months before points expire, in ``P[n]M`` RFC 3339 duration format. For example, a value of
    ``P12M`` represents a duration of 12 months. Points are valid through the last day of the month in which they are
    scheduled to expire. For example, with a ``P12M`` duration, points earned on July 6, 2020 expire on August 1,
    2021."""


class LoyaltyProgramExpirationPolicyDict(TypedDict):
    expiration_duration: str
