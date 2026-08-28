from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .subscription import Subscription, SubscriptionDict
from .subscription_action import SubscriptionAction, SubscriptionActionDict


class PauseSubscriptionResponse(SdkBaseModel):
    """Defines output parameters in a response from the `PauseSubscription
    <api-endpoint:Subscriptions-PauseSubscription>`__ endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered during the request."""

    subscription: Optional[Subscription] = UNSET
    """Represents a subscription purchased by a customer.

    For more information, see `Manage Subscriptions
    <https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions>`__."""

    actions: Optional[list[SubscriptionAction]] = UNSET
    """The list of a ``PAUSE`` action and a possible ``RESUME`` action created by the request."""


class PauseSubscriptionResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    subscription: NotRequired[Subscription | SubscriptionDict]
    actions: NotRequired[list[SubscriptionAction | SubscriptionActionDict]]
