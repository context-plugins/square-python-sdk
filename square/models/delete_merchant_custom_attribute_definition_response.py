from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DeleteMerchantCustomAttributeDefinitionResponse(SdkBaseModel):
    """Represents a response from a delete request containing error messages if there are any."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class DeleteMerchantCustomAttributeDefinitionResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
