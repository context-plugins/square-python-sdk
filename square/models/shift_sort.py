from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.shift_sort_field import ShiftSortFieldOrStr
from .enums.sort_order import SortOrderOrStr


class ShiftSort(SdkBaseModel):
    """Sets the sort order of search results.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    field: Optional[ShiftSortFieldOrStr] = UNSET
    """Enumerates the ``Shift`` fields to sort on.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    order: Optional[SortOrderOrStr] = UNSET
    """The order (e.g., chronological or alphabetical) in which results from a request are returned."""


class ShiftSortDict(TypedDict):
    field: NotRequired[ShiftSortFieldOrStr]
    order: NotRequired[SortOrderOrStr]
