from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class CalculateLoyaltyPointsRequest(SdkBaseModel):
    """Represents a `CalculateLoyaltyPoints <api-endpoint:Loyalty-CalculateLoyaltyPoints>`__ request."""

    order_id: OptionalNullable[str] = UNSET
    """The `order <entity:Order>`__ ID for which to calculate the points. Specify this field if your application uses
    the Orders API to process orders. Otherwise, specify the ``transaction_amount_money``."""

    transaction_amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    loyalty_account_id: OptionalNullable[str] = UNSET
    """The ID of the target `loyalty account <entity:LoyaltyAccount>`__. Optionally specify this field if your
    application uses the Orders API to process orders.

    If specified, the ``promotion_points`` field in the response shows the number of points the buyer would earn from
    the purchase. In this case, Square uses the account ID to determine whether the promotion's ``trigger_limit`` (the
    maximum number of times that a buyer can trigger the promotion) has been reached. If not specified, the
    ``promotion_points`` field shows the number of points the purchase qualifies for regardless of the trigger limit."""


class CalculateLoyaltyPointsRequestDict(TypedDict):
    order_id: NotRequired[str | None]
    transaction_amount_money: NotRequired[MoneyDict]
    loyalty_account_id: NotRequired[str | None]
