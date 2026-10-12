from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DeleteOrderCustomAttributeResponse(SdkBaseModel):
    """Represents a response from deleting an order custom attribute."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class DeleteOrderCustomAttributeResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
