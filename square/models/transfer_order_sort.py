from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sort_order import SortOrderOrStr
from .enums.transfer_order_sort_field import TransferOrderSortFieldOrStr


class TransferOrderSort(SdkBaseModel):
    """Sort configuration for search results"""

    field: Optional[TransferOrderSortFieldOrStr] = UNSET
    """Fields that can be used for sorting `TransferOrder <entity:TransferOrder>`__s in search results. Used with
    `SearchTransferOrders <api-endpoint:TransferOrders-SearchTransferOrders>`__ to control the order of returned
    results."""

    order: Optional[SortOrderOrStr] = UNSET
    """The order (e.g., chronological or alphabetical) in which results from a request are returned."""


class TransferOrderSortDict(TypedDict):
    field: NotRequired[TransferOrderSortFieldOrStr]
    order: NotRequired[SortOrderOrStr]
