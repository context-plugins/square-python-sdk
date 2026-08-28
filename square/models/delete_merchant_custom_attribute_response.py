from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DeleteMerchantCustomAttributeResponse(SdkBaseModel):
    """Represents a `DeleteMerchantCustomAttribute
    <api-endpoint:MerchantCustomAttributes-DeleteMerchantCustomAttribute>`__ response. Either an empty object ``{}``
    (for a successful deletion) or ``errors`` is present in the response."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class DeleteMerchantCustomAttributeResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
