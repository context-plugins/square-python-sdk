from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transfer_order_filter import TransferOrderFilter, TransferOrderFilterDict
from .transfer_order_sort import TransferOrderSort, TransferOrderSortDict


class TransferOrderQuery(SdkBaseModel):
    """Query parameters for searching transfer orders"""

    filter: Optional[TransferOrderFilter] = UNSET
    """Filter criteria for searching transfer orders"""

    sort: Optional[TransferOrderSort] = UNSET
    """Sort configuration for search results"""


class TransferOrderQueryDict(TypedDict):
    filter: NotRequired[TransferOrderFilter | TransferOrderFilterDict]
    sort: NotRequired[TransferOrderSort | TransferOrderSortDict]
