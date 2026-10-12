from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .subscription import Subscription, SubscriptionDict
from .subscription_action import SubscriptionAction, SubscriptionActionDict


class SwapPlanResponse(SdkBaseModel):
    """Defines output parameters in a response of the `SwapPlan <api-endpoint:Subscriptions-SwapPlan>`__ endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered during the request."""

    subscription: Optional[Subscription] = UNSET
    """Represents a subscription purchased by a customer.

    For more information, see `Manage Subscriptions
    <https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions>`__."""

    actions: Optional[list[SubscriptionAction]] = UNSET
    """A list of a ``SWAP_PLAN`` action created by the request."""


class SwapPlanResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    subscription: NotRequired[SubscriptionDict]
    actions: NotRequired[list[SubscriptionActionDict]]
