from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LoyaltyEventCreateReward(SdkBaseModel):
    """Provides metadata when the event ``type`` is ``CREATE_REWARD``."""

    loyalty_program_id: str
    """The ID of the `loyalty program <entity:LoyaltyProgram>`__."""

    reward_id: Optional[str] = UNSET
    """The Square-assigned ID of the created `loyalty reward <entity:LoyaltyReward>`__. This field is returned only if
    the event source is ``LOYALTY_API``."""

    points: int
    """The loyalty points used to create the reward."""


class LoyaltyEventCreateRewardDict(TypedDict):
    loyalty_program_id: str
    reward_id: NotRequired[str]
    points: int
