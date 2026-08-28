from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .subscription import Subscription, SubscriptionDict


class UpdateSubscriptionResponse(SdkBaseModel):
    """Defines output parameters in a response from the `UpdateSubscription
    <api-endpoint:Subscriptions-UpdateSubscription>`__ endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered during the request."""

    subscription: Optional[Subscription] = UNSET
    """Represents a subscription purchased by a customer.

    For more information, see `Manage Subscriptions
    <https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions>`__."""


class UpdateSubscriptionResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    subscription: NotRequired[Subscription | SubscriptionDict]
