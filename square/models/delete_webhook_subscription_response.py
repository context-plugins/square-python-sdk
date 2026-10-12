from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DeleteWebhookSubscriptionResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `DeleteWebhookSubscription
    <api-endpoint:WebhookSubscriptions-DeleteWebhookSubscription>`__ endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""


class DeleteWebhookSubscriptionResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
