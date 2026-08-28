from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.currency import CurrencyOrStr


class Money(SdkBaseModel):
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    amount: OptionalNullable[int] = UNSET
    """The amount of money, in the smallest denomination of the currency indicated by ``currency``. For example, when
    ``currency`` is ``USD``, ``amount`` is in cents. Monetary amounts can be positive or negative. See the specific
    field description to determine the meaning of the sign in a particular case."""

    currency: Optional[CurrencyOrStr] = UNSET
    """Indicates the associated currency for an amount of money. Values correspond to `ISO 4217
    <https://wikipedia.org/wiki/ISO_4217>`__."""


class MoneyDict(TypedDict):
    amount: NotRequired[int | None]
    currency: NotRequired[CurrencyOrStr]
