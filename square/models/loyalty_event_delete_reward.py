from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LoyaltyEventDeleteReward(SdkBaseModel):
    """Provides metadata when the event ``type`` is ``DELETE_REWARD``."""

    loyalty_program_id: str
    """The ID of the `loyalty program <entity:LoyaltyProgram>`__."""

    reward_id: Optional[str] = UNSET
    """The ID of the deleted `loyalty reward <entity:LoyaltyReward>`__. This field is returned only if the event source
    is ``LOYALTY_API``."""

    points: int
    """The number of points returned to the loyalty account."""


class LoyaltyEventDeleteRewardDict(TypedDict):
    loyalty_program_id: str
    reward_id: NotRequired[str]
    points: int
