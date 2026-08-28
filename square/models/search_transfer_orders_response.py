from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .transfer_order import TransferOrder, TransferOrderDict


class SearchTransferOrdersResponse(SdkBaseModel):
    """Response for searching transfer orders"""

    transfer_orders: Optional[list[TransferOrder]] = UNSET
    """List of transfer orders matching the search criteria"""

    cursor: Optional[str] = UNSET
    """Pagination cursor for fetching the next page of results"""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request"""


class SearchTransferOrdersResponseDict(TypedDict):
    transfer_orders: NotRequired[list[TransferOrder | TransferOrderDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]
