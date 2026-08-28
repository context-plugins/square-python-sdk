from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class AdditionalRecipient(SdkBaseModel):
    """Represents an additional recipient (other than the merchant) receiving a portion of this tender."""

    location_id: str
    """The location ID for a recipient (other than the merchant) receiving a portion of this tender."""

    description: OptionalNullable[str] = UNSET
    """The description of the additional recipient."""

    amount_money: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    receivable_id: OptionalNullable[str] = UNSET
    """The unique ID for the RETIRED ``AdditionalRecipientReceivable`` object. This field should be empty for any
    ``AdditionalRecipient`` objects created after the retirement."""


class AdditionalRecipientDict(TypedDict):
    location_id: str
    description: NotRequired[str | None]
    amount_money: Money | MoneyDict
    receivable_id: NotRequired[str | None]
