from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .loyalty_program import LoyaltyProgram, LoyaltyProgramDict


class ListLoyaltyProgramsResponse(SdkBaseModel):
    """A response that contains all loyalty programs."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    programs: Optional[list[LoyaltyProgram]] = UNSET
    """A list of ``LoyaltyProgram`` for the merchant."""


class ListLoyaltyProgramsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    programs: NotRequired[list[LoyaltyProgramDict]]
