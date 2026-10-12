from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DeleteCustomerCardResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the ``DeleteCustomerCard`` endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class DeleteCustomerCardResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
