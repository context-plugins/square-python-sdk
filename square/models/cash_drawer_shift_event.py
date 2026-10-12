from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.cash_drawer_event_type import CashDrawerEventTypeOrStr
from .money import Money, MoneyDict


class CashDrawerShiftEvent(SdkBaseModel):
    id: Optional[str] = UNSET
    """The unique ID of the event."""

    event_type: Optional[CashDrawerEventTypeOrStr] = UNSET
    """The types of events on a CashDrawerShift. Each event type represents an employee action on the actual cash drawer
    represented by a CashDrawerShift."""

    event_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    created_at: Optional[str] = UNSET
    """The event time in RFC 3339 format."""

    description: OptionalNullable[str] = UNSET
    """An optional description of the event, entered by the employee that created the event."""

    team_member_id: Optional[str] = UNSET
    """The ID of the team member that created the event."""


class CashDrawerShiftEventDict(TypedDict):
    id: NotRequired[str]
    event_type: NotRequired[CashDrawerEventTypeOrStr]
    event_money: NotRequired[MoneyDict]
    created_at: NotRequired[str]
    description: NotRequired[str | None]
    team_member_id: NotRequired[str]
