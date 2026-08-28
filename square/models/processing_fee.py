from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class ProcessingFee(SdkBaseModel):
    """Represents the Square processing fee."""

    effective_at: OptionalNullable[str] = UNSET
    """The timestamp of when the fee takes effect, in RFC 3339 format."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of fee assessed or adjusted. The fee type can be ``INITIAL`` or ``ADJUSTMENT``."""

    amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class ProcessingFeeDict(TypedDict):
    effective_at: NotRequired[str | None]
    type_: NotRequired[str | None]
    amount_money: NotRequired[Money | MoneyDict]
