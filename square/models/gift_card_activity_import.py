from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .money import Money, MoneyDict


class GiftCardActivityImport(SdkBaseModel):
    """Represents details about an ``IMPORT`` `gift card activity type <entity:GiftCardActivityType>`__. This activity
    type is used when Square imports a third-party gift card, in which case the ``gan_source`` of the gift card is set
    to ``OTHER``."""

    amount_money: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class GiftCardActivityImportDict(TypedDict):
    amount_money: MoneyDict
