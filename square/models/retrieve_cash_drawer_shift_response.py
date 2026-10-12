from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cash_drawer_shift import CashDrawerShift, CashDrawerShiftDict
from .error import Error, ErrorDict


class RetrieveCashDrawerShiftResponse(SdkBaseModel):
    cash_drawer_shift: Optional[CashDrawerShift] = UNSET
    """This model gives the details of a cash drawer shift. The cash_payment_money, cash_refund_money,
    cash_paid_in_money, and cash_paid_out_money fields are all computed by summing their respective event types."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class RetrieveCashDrawerShiftResponseDict(TypedDict):
    cash_drawer_shift: NotRequired[CashDrawerShiftDict]
    errors: NotRequired[list[ErrorDict]]
