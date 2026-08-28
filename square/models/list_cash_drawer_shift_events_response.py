from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .cash_drawer_shift_event import CashDrawerShiftEvent, CashDrawerShiftEventDict
from .error import Error, ErrorDict


class ListCashDrawerShiftEventsResponse(SdkBaseModel):
    cursor: Optional[str] = UNSET
    """Opaque cursor for fetching the next page. Cursor is not present in the last page of results."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    cash_drawer_shift_events: Optional[list[CashDrawerShiftEvent]] = UNSET
    """All of the events (payments, refunds, etc.) for a cash drawer during the shift."""


class ListCashDrawerShiftEventsResponseDict(TypedDict):
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]
    cash_drawer_shift_events: NotRequired[list[CashDrawerShiftEvent | CashDrawerShiftEventDict]]
