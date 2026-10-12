from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payout import Payout, PayoutDict


class PayoutFailedEventObject(SdkBaseModel):
    payout: Optional[Payout] = UNSET
    """An accounting of the amount owed the seller and record of the actual transfer to their external bank account or
    to the Square balance."""


class PayoutFailedEventObjectDict(TypedDict):
    payout: NotRequired[PayoutDict]
