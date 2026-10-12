from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .subscription import Subscription, SubscriptionDict


class UpdateSubscriptionRequest(SdkBaseModel):
    """Defines input parameters in a request to the `UpdateSubscription
    <api-endpoint:Subscriptions-UpdateSubscription>`__ endpoint."""

    subscription: Optional[Subscription] = UNSET
    """Represents a subscription purchased by a customer.

    For more information, see `Manage Subscriptions
    <https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions>`__."""


class UpdateSubscriptionRequestDict(TypedDict):
    subscription: NotRequired[SubscriptionDict]
