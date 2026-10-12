from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class CheckoutLocationSettingsTipping(SdkBaseModel):
    percentages: OptionalNullable[list[int]] = UNSET
    """Set three custom percentage amounts that buyers can select at checkout. If Smart Tip is enabled, this only
    applies to transactions totaling $10 or more."""

    smart_tipping_enabled: OptionalNullable[bool] = UNSET
    """Enables Smart Tip Amounts. If Smart Tip Amounts is enabled, tipping works as follows: If a transaction is less
    than $10, the available tipping options include No Tip, $1, $2, or $3. If a transaction is $10 or more, the
    available tipping options include No Tip, 15%, 20%, or 25%. You can set custom percentage amounts with the
    ``percentages`` field."""

    default_percent: OptionalNullable[int] = UNSET
    """Set the pre-selected percentage amounts that appear at checkout. If Smart Tip is enabled, this only applies to
    transactions totaling $10 or more."""

    smart_tips: OptionalNullable[list[Money]] = UNSET
    """Show the Smart Tip Amounts for this location."""

    default_smart_tip: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class CheckoutLocationSettingsTippingDict(TypedDict):
    percentages: NotRequired[list[int] | None]
    smart_tipping_enabled: NotRequired[bool | None]
    default_percent: NotRequired[int | None]
    smart_tips: NotRequired[list[MoneyDict] | None]
    default_smart_tip: NotRequired[MoneyDict]
