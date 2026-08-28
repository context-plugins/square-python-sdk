from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_attribute import CustomAttribute, CustomAttributeDict
from .error import Error, ErrorDict


class UpsertOrderCustomAttributeResponse(SdkBaseModel):
    """Represents a response from upserting order custom attribute definitions."""

    custom_attribute: Optional[CustomAttribute] = UNSET
    """A custom attribute value. Each custom attribute value has a corresponding ``CustomAttributeDefinition``
    object."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class UpsertOrderCustomAttributeResponseDict(TypedDict):
    custom_attribute: NotRequired[CustomAttribute | CustomAttributeDict]
    errors: NotRequired[list[Error | ErrorDict]]
