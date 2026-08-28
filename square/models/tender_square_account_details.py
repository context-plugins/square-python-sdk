from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.tender_square_account_details_status import TenderSquareAccountDetailsStatusOrStr


class TenderSquareAccountDetails(SdkBaseModel):
    """Represents the details of a tender with ``type`` ``SQUARE_ACCOUNT``."""

    status: Optional[TenderSquareAccountDetailsStatusOrStr] = UNSET


class TenderSquareAccountDetailsDict(TypedDict):
    status: NotRequired[TenderSquareAccountDetailsStatusOrStr]
