from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.loyalty_promotion_status import LoyaltyPromotionStatusOrStr
from .loyalty_promotion_available_time_data import (
    LoyaltyPromotionAvailableTimeData,
    LoyaltyPromotionAvailableTimeDataDict,
)
from .loyalty_promotion_incentive import LoyaltyPromotionIncentive, LoyaltyPromotionIncentiveDict
from .loyalty_promotion_trigger_limit import LoyaltyPromotionTriggerLimit, LoyaltyPromotionTriggerLimitDict
from .money import Money, MoneyDict


class LoyaltyPromotion(SdkBaseModel):
    """Represents a promotion for a `loyalty program <entity:LoyaltyProgram>`__. Loyalty promotions enable buyers to
    earn extra points on top of those earned from the base program.

    A loyalty program can have a maximum of 10 loyalty promotions with an ``ACTIVE`` or ``SCHEDULED`` status."""

    id: Optional[str] = UNSET
    """The Square-assigned ID of the promotion."""

    name: str
    """The name of the promotion."""

    incentive: LoyaltyPromotionIncentive
    """Represents how points for a `loyalty promotion <entity:LoyaltyPromotion>`__ are calculated, either by multiplying
    the points earned from the base program or by adding a specified number of points to the points earned from the base
    program."""

    available_time: LoyaltyPromotionAvailableTimeData
    """Represents scheduling information that determines when purchases can qualify to earn points from a `loyalty
    promotion <entity:LoyaltyPromotion>`__."""

    trigger_limit: Optional[LoyaltyPromotionTriggerLimit] = UNSET
    """Represents the number of times a buyer can earn points during a `loyalty promotion <entity:LoyaltyPromotion>`__.
    If this field is not set, buyers can trigger the promotion an unlimited number of times to earn points during the
    time that the promotion is available.

    A purchase that is disqualified from earning points because of this limit might qualify for another active
    promotion."""

    status: Optional[LoyaltyPromotionStatusOrStr] = UNSET
    """Indicates the status of a `loyalty promotion <entity:LoyaltyPromotion>`__."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the promotion was created, in RFC 3339 format."""

    canceled_at: Optional[str] = UNSET
    """The timestamp of when the promotion was canceled, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp when the promotion was last updated, in RFC 3339 format."""

    loyalty_program_id: Optional[str] = UNSET
    """The ID of the `loyalty program <entity:LoyaltyProgram>`__ associated with the promotion."""

    minimum_spend_amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    qualifying_item_variation_ids: OptionalNullable[list[str]] = UNSET
    """The IDs of any qualifying ``ITEM_VARIATION`` `catalog objects <entity:CatalogObject>`__. If specified, the
    purchase must include at least one of these items to qualify for the promotion.

    This option is valid only if the base loyalty program uses a ``VISIT`` or ``SPEND`` accrual rule. With ``SPEND``
    accrual rules, make sure that qualifying promotional items are not excluded.

    You can specify ``qualifying_item_variation_ids`` or ``qualifying_category_ids`` for a given promotion, but not
    both."""

    qualifying_category_ids: OptionalNullable[list[str]] = UNSET
    """The IDs of any qualifying ``CATEGORY`` `catalog objects <entity:CatalogObject>`__. If specified, the purchase
    must include at least one item from one of these categories to qualify for the promotion.

    This option is valid only if the base loyalty program uses a ``VISIT`` or ``SPEND`` accrual rule. With ``SPEND``
    accrual rules, make sure that qualifying promotional items are not excluded.

    You can specify ``qualifying_category_ids`` or ``qualifying_item_variation_ids`` for a promotion, but not both."""


class LoyaltyPromotionDict(TypedDict):
    id: NotRequired[str]
    name: str
    incentive: LoyaltyPromotionIncentiveDict
    available_time: LoyaltyPromotionAvailableTimeDataDict
    trigger_limit: NotRequired[LoyaltyPromotionTriggerLimitDict]
    status: NotRequired[LoyaltyPromotionStatusOrStr]
    created_at: NotRequired[str]
    canceled_at: NotRequired[str]
    updated_at: NotRequired[str]
    loyalty_program_id: NotRequired[str]
    minimum_spend_amount_money: NotRequired[MoneyDict]
    qualifying_item_variation_ids: NotRequired[list[str] | None]
    qualifying_category_ids: NotRequired[list[str] | None]
