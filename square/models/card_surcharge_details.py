from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict


class CardSurchargeDetails(SdkBaseModel):
    """Details related to an attempt to apply a card surcharge to this payment. When surcharge eligibility is not known
    in advance, such as when the card type (debit or credit) is required to make the eligibility determination,
    proposed_card_surcharge_money and proposed_additional_amount_money will match the values in the request, while
    card_surcharge_money and additional_amount_money are present only when the payment has a surcharge applied."""

    card_surcharge_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class CardSurchargeDetailsDict(TypedDict):
    card_surcharge_money: NotRequired[Money | MoneyDict]
