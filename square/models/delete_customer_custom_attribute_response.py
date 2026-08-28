from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DeleteCustomerCustomAttributeResponse(SdkBaseModel):
    """Represents a `DeleteCustomerCustomAttribute
    <api-endpoint:CustomerCustomAttributes-DeleteCustomerCustomAttribute>`__ response. Either an empty object ``{}``
    (for a successful deletion) or ``errors`` is present in the response."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class DeleteCustomerCustomAttributeResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
