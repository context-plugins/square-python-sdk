from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class UpdateWebhookSubscriptionSignatureKeyResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the
    `UpdateWebhookSubscriptionSignatureKey <api-endpoint:WebhookSubscriptions-UpdateWebhookSubscriptionSignatureKey>`__
    endpoint.

    Note: If there are errors processing the request, the `Subscription <entity:WebhookSubscription>`__ is not
    present."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    signature_key: Optional[str] = UNSET
    """The new Square-generated signature key used to validate the origin of the webhook event."""


class UpdateWebhookSubscriptionSignatureKeyResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    signature_key: NotRequired[str]
