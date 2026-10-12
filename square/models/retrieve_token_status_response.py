from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class RetrieveTokenStatusResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the ``RetrieveTokenStatus``
    endpoint."""

    scopes: Optional[list[str]] = UNSET
    """The list of scopes associated with an access token."""

    expires_at: Optional[str] = UNSET
    """The date and time when the ``access_token`` expires, in RFC 3339 format. Empty if the token never expires."""

    client_id: Optional[str] = UNSET
    """The Square-issued application ID associated with the access token. This is the same application ID used to obtain
    the token."""

    merchant_id: Optional[str] = UNSET
    """The ID of the authorizing merchant's business."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class RetrieveTokenStatusResponseDict(TypedDict):
    scopes: NotRequired[list[str]]
    expires_at: NotRequired[str]
    client_id: NotRequired[str]
    merchant_id: NotRequired[str]
    errors: NotRequired[list[ErrorDict]]
