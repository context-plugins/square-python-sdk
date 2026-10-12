from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.catalog_quick_amount_type import CatalogQuickAmountTypeOrStr
from .money import Money, MoneyDict


class CatalogQuickAmount(SdkBaseModel):
    """Represents a Quick Amount in the Catalog."""

    type_: CatalogQuickAmountTypeOrStr = Field(alias="type")
    """Determines the type of a specific Quick Amount."""

    amount: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    score: OptionalNullable[int] = UNSET
    """Describes the ranking of the Quick Amount provided by machine learning model, in the range [0, 100]. MANUAL type
    amount will always have score = 100."""

    ordinal: OptionalNullable[int] = UNSET
    """The order in which this Quick Amount should be displayed."""


class CatalogQuickAmountDict(TypedDict):
    type_: CatalogQuickAmountTypeOrStr
    amount: MoneyDict
    score: NotRequired[int | None]
    ordinal: NotRequired[int | None]
