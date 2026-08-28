from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class OrderLineItemAppliedServiceCharge(SdkBaseModel):
    uid: OptionalNullable[str] = UNSET
    """A unique ID that identifies the applied service charge only within this order."""

    service_charge_uid: str
    """The ``uid`` of the service charge that the applied service charge represents. It must reference a service charge
    present in the ``order.service_charges`` field.

    This field is immutable. To change which service charges apply to a line item, delete and add a new
    ``OrderLineItemAppliedServiceCharge``."""

    applied_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class OrderLineItemAppliedServiceChargeDict(TypedDict):
    uid: NotRequired[str | None]
    service_charge_uid: str
    applied_money: NotRequired[Money | MoneyDict]
