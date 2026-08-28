from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class LoyaltyEventAdjustPoints(SdkBaseModel):
    """Provides metadata when the event ``type`` is ``ADJUST_POINTS``."""

    loyalty_program_id: Optional[str] = UNSET
    """The Square-assigned ID of the `loyalty program <entity:LoyaltyProgram>`__."""

    points: int
    """The number of points added or removed."""

    reason: OptionalNullable[str] = UNSET
    """The reason for the adjustment of points."""


class LoyaltyEventAdjustPointsDict(TypedDict):
    loyalty_program_id: NotRequired[str]
    points: int
    reason: NotRequired[str | None]
