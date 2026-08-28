from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.cash_drawer_shift_state import CashDrawerShiftStateOrStr
from .money import Money, MoneyDict


class CashDrawerShiftSummary(SdkBaseModel):
    """The summary of a closed cash drawer shift. This model contains only the money counted to start a cash drawer
    shift, counted at the end of the shift, and the amount that should be in the drawer at shift end based on summing
    all cash drawer shift events."""

    id: Optional[str] = UNSET
    """The shift unique ID."""

    state: Optional[CashDrawerShiftStateOrStr] = UNSET
    """The current state of a cash drawer shift."""

    opened_at: OptionalNullable[str] = UNSET
    """The shift start time in ISO 8601 format."""

    ended_at: OptionalNullable[str] = UNSET
    """The shift end time in ISO 8601 format."""

    closed_at: OptionalNullable[str] = UNSET
    """The shift close time in ISO 8601 format."""

    description: OptionalNullable[str] = UNSET
    """An employee free-text description of a cash drawer shift."""

    opened_cash_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    expected_cash_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    closed_cash_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    created_at: Optional[str] = UNSET
    """The shift start time in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The shift updated at time in RFC 3339 format."""

    location_id: Optional[str] = UNSET
    """The ID of the location the cash drawer shift belongs to."""


class CashDrawerShiftSummaryDict(TypedDict):
    id: NotRequired[str]
    state: NotRequired[CashDrawerShiftStateOrStr]
    opened_at: NotRequired[str | None]
    ended_at: NotRequired[str | None]
    closed_at: NotRequired[str | None]
    description: NotRequired[str | None]
    opened_cash_money: NotRequired[Money | MoneyDict]
    expected_cash_money: NotRequired[Money | MoneyDict]
    closed_cash_money: NotRequired[Money | MoneyDict]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    location_id: NotRequired[str]
