from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.subscription_cadence import SubscriptionCadenceOrStr
from .money import Money, MoneyDict
from .subscription_pricing import SubscriptionPricing, SubscriptionPricingDict


class SubscriptionPhase(SdkBaseModel):
    """Describes a phase in a subscription plan variation. For more information, see `Subscription Plans and Variations
    <https://developer.squareup.com/docs/subscriptions-api/plans-and-variations>`__."""

    uid: OptionalNullable[str] = UNSET
    """The Square-assigned ID of the subscription phase. This field cannot be changed after a ``SubscriptionPhase`` is
    created."""

    cadence: SubscriptionCadenceOrStr
    """Determines the billing cadence of a `Subscription <entity:Subscription>`__"""

    periods: OptionalNullable[int] = UNSET
    """The number of ``cadence``s the phase lasts. If not set, the phase never ends. Only the last phase can be
    indefinite. This field cannot be changed after a ``SubscriptionPhase`` is created."""

    recurring_price_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    ordinal: OptionalNullable[int] = UNSET
    """The position this phase appears in the sequence of phases defined for the plan, indexed from 0. This field cannot
    be changed after a ``SubscriptionPhase`` is created."""

    pricing: Optional[SubscriptionPricing] = UNSET
    """Describes the pricing for the subscription."""


class SubscriptionPhaseDict(TypedDict):
    uid: NotRequired[str | None]
    cadence: SubscriptionCadenceOrStr
    periods: NotRequired[int | None]
    recurring_price_money: NotRequired[Money | MoneyDict]
    ordinal: NotRequired[int | None]
    pricing: NotRequired[SubscriptionPricing | SubscriptionPricingDict]
