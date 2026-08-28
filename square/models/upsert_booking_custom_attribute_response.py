from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_attribute import CustomAttribute, CustomAttributeDict
from .error import Error, ErrorDict


class UpsertBookingCustomAttributeResponse(SdkBaseModel):
    """Represents an `UpsertBookingCustomAttribute
    <api-endpoint:BookingCustomAttributes-UpsertBookingCustomAttribute>`__ response. Either
    ``custom_attribute_definition`` or ``errors`` is present in the response."""

    custom_attribute: Optional[CustomAttribute] = UNSET
    """A custom attribute value. Each custom attribute value has a corresponding ``CustomAttributeDefinition``
    object."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class UpsertBookingCustomAttributeResponseDict(TypedDict):
    custom_attribute: NotRequired[CustomAttribute | CustomAttributeDict]
    errors: NotRequired[list[Error | ErrorDict]]
