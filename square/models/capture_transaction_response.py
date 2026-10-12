from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class CaptureTransactionResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `CaptureTransaction
    <api-endpoint:Transactions-CaptureTransaction>`__ endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class CaptureTransactionResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
