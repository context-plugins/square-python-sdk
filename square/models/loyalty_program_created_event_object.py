from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_program import LoyaltyProgram, LoyaltyProgramDict


class LoyaltyProgramCreatedEventObject(SdkBaseModel):
    """An object that contains the loyalty program associated with a ``loyalty.program.created`` event."""

    loyalty_program: Optional[LoyaltyProgram] = UNSET
    """Represents a Square loyalty program. Loyalty programs define how buyers can earn points and redeem points for
    rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard.
    For more information, see `Loyalty Program Overview <https://developer.squareup.com/docs/loyalty/overview>`__."""


class LoyaltyProgramCreatedEventObjectDict(TypedDict):
    loyalty_program: NotRequired[LoyaltyProgram | LoyaltyProgramDict]
