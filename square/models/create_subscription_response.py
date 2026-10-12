from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .subscription import Subscription, SubscriptionDict


class CreateSubscriptionResponse(SdkBaseModel):
    """Defines output parameters in a response from the `CreateSubscription
    <api-endpoint:Subscriptions-CreateSubscription>`__ endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered during the request."""

    subscription: Optional[Subscription] = UNSET
    """Represents a subscription purchased by a customer.

    For more information, see `Manage Subscriptions
    <https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions>`__."""


class CreateSubscriptionResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    subscription: NotRequired[SubscriptionDict]
