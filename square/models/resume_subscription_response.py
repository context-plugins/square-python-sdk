from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .subscription import Subscription, SubscriptionDict
from .subscription_action import SubscriptionAction, SubscriptionActionDict


class ResumeSubscriptionResponse(SdkBaseModel):
    """Defines output parameters in a response from the `ResumeSubscription
    <api-endpoint:Subscriptions-ResumeSubscription>`__ endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered during the request."""

    subscription: Optional[Subscription] = UNSET
    """Represents a subscription purchased by a customer.

    For more information, see `Manage Subscriptions
    <https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions>`__."""

    actions: Optional[list[SubscriptionAction]] = UNSET
    """A list of ``RESUME`` actions created by the request and scheduled for the subscription."""


class ResumeSubscriptionResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    subscription: NotRequired[SubscriptionDict]
    actions: NotRequired[list[SubscriptionActionDict]]
