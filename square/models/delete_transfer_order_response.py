from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DeleteTransferOrderResponse(SdkBaseModel):
    """Response for deleting a transfer order"""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request"""


class DeleteTransferOrderResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
