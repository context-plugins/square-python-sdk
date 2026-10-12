from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cash_drawer_shift_summary import CashDrawerShiftSummary, CashDrawerShiftSummaryDict
from .error import Error, ErrorDict


class ListCashDrawerShiftsResponse(SdkBaseModel):
    cursor: Optional[str] = UNSET
    """Opaque cursor for fetching the next page of results. Cursor is not present in the last page of results."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    cash_drawer_shifts: Optional[list[CashDrawerShiftSummary]] = UNSET
    """A collection of CashDrawerShiftSummary objects for shifts that match the query."""


class ListCashDrawerShiftsResponseDict(TypedDict):
    cursor: NotRequired[str]
    errors: NotRequired[list[ErrorDict]]
    cash_drawer_shifts: NotRequired[list[CashDrawerShiftSummaryDict]]
