from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_attribute import CustomAttribute, CustomAttributeDict
from .error import Error, ErrorDict


class UpsertLocationCustomAttributeResponse(SdkBaseModel):
    """Represents an `UpsertLocationCustomAttribute
    <api-endpoint:LocationCustomAttributes-UpsertLocationCustomAttribute>`__ response. Either
    ``custom_attribute_definition`` or ``errors`` is present in the response."""

    custom_attribute: Optional[CustomAttribute] = UNSET
    """A custom attribute value. Each custom attribute value has a corresponding ``CustomAttributeDefinition``
    object."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class UpsertLocationCustomAttributeResponseDict(TypedDict):
    custom_attribute: NotRequired[CustomAttributeDict]
    errors: NotRequired[list[ErrorDict]]
