from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.batch_retrieve_inventory_changes_sort_field import BatchRetrieveInventoryChangesSortFieldOrStr
from .enums.sort_order import SortOrderOrStr


class BatchRetrieveInventoryChangesSort(SdkBaseModel):
    field: Optional[BatchRetrieveInventoryChangesSortFieldOrStr] = UNSET
    order: Optional[SortOrderOrStr] = UNSET
    """The order (e.g., chronological or alphabetical) in which results from a request are returned."""


class BatchRetrieveInventoryChangesSortDict(TypedDict):
    field: NotRequired[BatchRetrieveInventoryChangesSortFieldOrStr]
    order: NotRequired[SortOrderOrStr]
