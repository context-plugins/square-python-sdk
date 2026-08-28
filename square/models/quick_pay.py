from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .money import Money, MoneyDict


class QuickPay(SdkBaseModel):
    """Describes an ad hoc item and price to generate a quick pay checkout link. For more information, see `Quick Pay
    Checkout <https://developer.squareup.com/docs/checkout-api/quick-pay-checkout>`__."""

    name: str
    """The ad hoc item name. In the resulting ``Order``, this name appears as the line item name."""

    price_money: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    location_id: str
    """The ID of the business location the checkout is associated with."""


class QuickPayDict(TypedDict):
    name: str
    price_money: Money | MoneyDict
    location_id: str
