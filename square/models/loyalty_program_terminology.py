from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LoyaltyProgramTerminology(SdkBaseModel):
    """Represents the naming used for loyalty points."""

    one: str
    """A singular unit for a point (for example, 1 point is called 1 star)."""

    other: str
    """A plural unit for point (for example, 10 points is called 10 stars)."""


class LoyaltyProgramTerminologyDict(TypedDict):
    one: str
    other: str
