from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_attribute import CustomAttribute, CustomAttributeDict
from .error import Error, ErrorDict


class RetrieveOrderCustomAttributeResponse(SdkBaseModel):
    """Represents a response from getting an order custom attribute."""

    custom_attribute: Optional[CustomAttribute] = UNSET
    """A custom attribute value. Each custom attribute value has a corresponding ``CustomAttributeDefinition``
    object."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class RetrieveOrderCustomAttributeResponseDict(TypedDict):
    custom_attribute: NotRequired[CustomAttributeDict]
    errors: NotRequired[list[ErrorDict]]
