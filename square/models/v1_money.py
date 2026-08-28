from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.currency import CurrencyOrStr


class V1Money(SdkBaseModel):
    amount: OptionalNullable[int] = UNSET
    """Amount in the lowest denominated value of this Currency. E.g. in USD these are cents, in JPY they are Yen (which
    do not have a 'cent' concept)."""

    currency_code: Optional[CurrencyOrStr] = UNSET
    """Indicates the associated currency for an amount of money. Values correspond to `ISO 4217
    <https://wikipedia.org/wiki/ISO_4217>`__."""


class V1MoneyDict(TypedDict):
    amount: NotRequired[int | None]
    currency_code: NotRequired[CurrencyOrStr]
