from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .subscription import Subscription, SubscriptionDict
from .subscription_action import SubscriptionAction, SubscriptionActionDict


class ChangeBillingAnchorDateResponse(SdkBaseModel):
    """Defines output parameters in a request to the `ChangeBillingAnchorDate
    <api-endpoint:Subscriptions-ChangeBillingAnchorDate>`__ endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered during the request."""

    subscription: Optional[Subscription] = UNSET
    """Represents a subscription purchased by a customer.

    For more information, see `Manage Subscriptions
    <https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions>`__."""

    actions: Optional[list[SubscriptionAction]] = UNSET
    """A list of a single billing anchor date change for the subscription."""


class ChangeBillingAnchorDateResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    subscription: NotRequired[SubscriptionDict]
    actions: NotRequired[list[SubscriptionActionDict]]
