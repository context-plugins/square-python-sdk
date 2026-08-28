from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .cash_drawer_device import CashDrawerDevice, CashDrawerDeviceDict
from .enums.cash_drawer_shift_state import CashDrawerShiftStateOrStr
from .money import Money, MoneyDict


class CashDrawerShift(SdkBaseModel):
    """This model gives the details of a cash drawer shift. The cash_payment_money, cash_refund_money,
    cash_paid_in_money, and cash_paid_out_money fields are all computed by summing their respective event types."""

    id: Optional[str] = UNSET
    """The shift unique ID."""

    state: Optional[CashDrawerShiftStateOrStr] = UNSET
    """The current state of a cash drawer shift."""

    opened_at: OptionalNullable[str] = UNSET
    """The time when the shift began, in ISO 8601 format."""

    ended_at: OptionalNullable[str] = UNSET
    """The time when the shift ended, in ISO 8601 format."""

    closed_at: OptionalNullable[str] = UNSET
    """The time when the shift was closed, in ISO 8601 format."""

    description: OptionalNullable[str] = UNSET
    """The free-form text description of a cash drawer by an employee."""

    opened_cash_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    cash_payment_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    cash_refunds_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    cash_paid_in_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    cash_paid_out_money: Optional[Money] = UNSET
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

    device: Optional[CashDrawerDevice] = UNSET
    created_at: Optional[str] = UNSET
    """The shift start time in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The shift updated at time in RFC 3339 format."""

    location_id: Optional[str] = UNSET
    """The ID of the location the cash drawer shift belongs to."""

    team_member_ids: Optional[list[str]] = UNSET
    """The IDs of all team members that were logged into Square Point of Sale at any point while the cash drawer shift
    was open."""

    opening_team_member_id: Optional[str] = UNSET
    """The ID of the team member that started the cash drawer shift."""

    ending_team_member_id: Optional[str] = UNSET
    """The ID of the team member that ended the cash drawer shift."""

    closing_team_member_id: Optional[str] = UNSET
    """The ID of the team member that closed the cash drawer shift by auditing the cash drawer contents."""


class CashDrawerShiftDict(TypedDict):
    id: NotRequired[str]
    state: NotRequired[CashDrawerShiftStateOrStr]
    opened_at: NotRequired[str | None]
    ended_at: NotRequired[str | None]
    closed_at: NotRequired[str | None]
    description: NotRequired[str | None]
    opened_cash_money: NotRequired[Money | MoneyDict]
    cash_payment_money: NotRequired[Money | MoneyDict]
    cash_refunds_money: NotRequired[Money | MoneyDict]
    cash_paid_in_money: NotRequired[Money | MoneyDict]
    cash_paid_out_money: NotRequired[Money | MoneyDict]
    expected_cash_money: NotRequired[Money | MoneyDict]
    closed_cash_money: NotRequired[Money | MoneyDict]
    device: NotRequired[CashDrawerDevice | CashDrawerDeviceDict]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    location_id: NotRequired[str]
    team_member_ids: NotRequired[list[str]]
    opening_team_member_id: NotRequired[str]
    ending_team_member_id: NotRequired[str]
    closing_team_member_id: NotRequired[str]
