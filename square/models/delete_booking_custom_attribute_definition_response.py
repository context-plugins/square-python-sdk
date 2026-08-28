from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DeleteBookingCustomAttributeDefinitionResponse(SdkBaseModel):
    """Represents a `DeleteBookingCustomAttributeDefinition
    <api-endpoint:BookingCustomAttributes-DeleteBookingCustomAttributeDefinition>`__ response containing error messages
    when errors occurred during the request. The successful response does not contain any payload."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class DeleteBookingCustomAttributeDefinitionResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
