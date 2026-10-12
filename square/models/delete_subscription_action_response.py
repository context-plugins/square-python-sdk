from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .subscription import Subscription, SubscriptionDict


class DeleteSubscriptionActionResponse(SdkBaseModel):
    """Defines output parameters in a response of the `DeleteSubscriptionAction
    <api-endpoint:Subscriptions-DeleteSubscriptionAction>`__ endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered during the request."""

    subscription: Optional[Subscription] = UNSET
    """Represents a subscription purchased by a customer.

    For more information, see `Manage Subscriptions
    <https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions>`__."""


class DeleteSubscriptionActionResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    subscription: NotRequired[SubscriptionDict]
