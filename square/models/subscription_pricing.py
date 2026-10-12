from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.subscription_pricing_type import SubscriptionPricingTypeOrStr
from .money import Money, MoneyDict


class SubscriptionPricing(SdkBaseModel):
    """Describes the pricing for the subscription."""

    type_: Optional[SubscriptionPricingTypeOrStr] = Field(default=UNSET, alias="type")
    """Determines the pricing of a `Subscription <entity:Subscription>`__"""

    discount_ids: OptionalNullable[list[str]] = UNSET
    """The ids of the discount catalog objects"""

    price_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class SubscriptionPricingDict(TypedDict):
    type_: NotRequired[SubscriptionPricingTypeOrStr]
    discount_ids: NotRequired[list[str] | None]
    price_money: NotRequired[MoneyDict]
