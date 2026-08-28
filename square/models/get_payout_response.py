from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .payout import Payout, PayoutDict


class GetPayoutResponse(SdkBaseModel):
    payout: Optional[Payout] = UNSET
    """An accounting of the amount owed the seller and record of the actual transfer to their external bank account or
    to the Square balance."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""


class GetPayoutResponseDict(TypedDict):
    payout: NotRequired[Payout | PayoutDict]
    errors: NotRequired[list[Error | ErrorDict]]
