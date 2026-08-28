from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .loyalty_program import LoyaltyProgram, LoyaltyProgramDict


class RetrieveLoyaltyProgramResponse(SdkBaseModel):
    """A response that contains the loyalty program."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    program: Optional[LoyaltyProgram] = UNSET
    """Represents a Square loyalty program. Loyalty programs define how buyers can earn points and redeem points for
    rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard.
    For more information, see `Loyalty Program Overview <https://developer.squareup.com/docs/loyalty/overview>`__."""


class RetrieveLoyaltyProgramResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    program: NotRequired[LoyaltyProgram | LoyaltyProgramDict]
