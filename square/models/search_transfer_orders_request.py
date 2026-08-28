from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transfer_order_query import TransferOrderQuery, TransferOrderQueryDict


class SearchTransferOrdersRequest(SdkBaseModel):
    """Request to search transfer orders"""

    query: Optional[TransferOrderQuery] = UNSET
    """Query parameters for searching transfer orders"""

    cursor: Optional[str] = UNSET
    """Pagination cursor from a previous search response"""

    limit: Optional[int] = UNSET
    """Maximum number of results to return (1-100)"""


class SearchTransferOrdersRequestDict(TypedDict):
    query: NotRequired[TransferOrderQuery | TransferOrderQueryDict]
    cursor: NotRequired[str]
    limit: NotRequired[int]
