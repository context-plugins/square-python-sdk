from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .subscription_test_result import SubscriptionTestResult, SubscriptionTestResultDict


class TestWebhookSubscriptionResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `TestWebhookSubscription
    <api-endpoint:WebhookSubscriptions-TestWebhookSubscription>`__ endpoint.

    Note: If there are errors processing the request, the `SubscriptionTestResult <entity:SubscriptionTestResult>`__
    field is not present."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    subscription_test_result: Optional[SubscriptionTestResult] = UNSET
    """Represents the details of a webhook subscription, including notification URL, event types, and signature key."""


class TestWebhookSubscriptionResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    subscription_test_result: NotRequired[SubscriptionTestResult | SubscriptionTestResultDict]
