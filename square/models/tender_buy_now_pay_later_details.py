from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.tender_buy_now_pay_later_details_brand import TenderBuyNowPayLaterDetailsBrandOrStr
from .enums.tender_buy_now_pay_later_details_status import TenderBuyNowPayLaterDetailsStatusOrStr


class TenderBuyNowPayLaterDetails(SdkBaseModel):
    """Represents the details of a tender with ``type`` ``BUY_NOW_PAY_LATER``."""

    buy_now_pay_later_brand: Optional[TenderBuyNowPayLaterDetailsBrandOrStr] = UNSET
    status: Optional[TenderBuyNowPayLaterDetailsStatusOrStr] = UNSET


class TenderBuyNowPayLaterDetailsDict(TypedDict):
    buy_now_pay_later_brand: NotRequired[TenderBuyNowPayLaterDetailsBrandOrStr]
    status: NotRequired[TenderBuyNowPayLaterDetailsStatusOrStr]
