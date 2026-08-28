from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order import Order, OrderDict
from .order_reward import OrderReward, OrderRewardDict


class CalculateOrderRequest(SdkBaseModel):
    order: Order
    """Contains all information related to a single order to process with Square, including line items that specify the
    products to purchase. ``Order`` objects also include information about any associated tenders, refunds, and returns.

    All Connect V2 Transactions have all been converted to Orders including all associated itemization data."""

    proposed_rewards: Optional[list[OrderReward | None]] = UNSET
    """Identifies one or more loyalty reward tiers to apply during the order calculation. The discounts defined by the
    reward tiers are added to the order only to preview the effect of applying the specified rewards. The rewards do not
    correspond to actual redemptions; that is, no ``reward``s are created. Therefore, the reward ``id``s are random
    strings used only to reference the reward tier."""


class CalculateOrderRequestDict(TypedDict):
    order: Order | OrderDict
    proposed_rewards: NotRequired[list[OrderReward | OrderRewardDict | None]]
