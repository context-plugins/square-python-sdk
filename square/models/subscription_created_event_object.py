from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .subscription import Subscription, SubscriptionDict


class SubscriptionCreatedEventObject(SdkBaseModel):
    subscription: Optional[Subscription] = UNSET
    """Represents a subscription purchased by a customer.

    For more information, see `Manage Subscriptions
    <https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions>`__."""


class SubscriptionCreatedEventObjectDict(TypedDict):
    subscription: NotRequired[SubscriptionDict]
