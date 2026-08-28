from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sort_order import SortOrderOrStr


class TerminalCheckoutQuerySort(SdkBaseModel):
    sort_order: Optional[SortOrderOrStr] = UNSET
    """The order (e.g., chronological or alphabetical) in which results from a request are returned."""


class TerminalCheckoutQuerySortDict(TypedDict):
    sort_order: NotRequired[SortOrderOrStr]
