from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .money import Money, MoneyDict


class ChargeRequestAdditionalRecipient(SdkBaseModel):
    """Represents an additional recipient (other than the merchant) entitled to a portion of the tender. Support is
    currently limited to USD, CAD and GBP currencies"""

    location_id: str
    """The location ID for a recipient (other than the merchant) receiving a portion of the tender."""

    description: str
    """The description of the additional recipient."""

    amount_money: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class ChargeRequestAdditionalRecipientDict(TypedDict):
    location_id: str
    description: str
    amount_money: Money | MoneyDict
