from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shift_filter import ShiftFilter, ShiftFilterDict
from .shift_sort import ShiftSort, ShiftSortDict


class ShiftQuery(SdkBaseModel):
    """The parameters of a ``Shift`` search query, which includes filter and sort options.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    filter: Optional[ShiftFilter] = UNSET
    """Defines a filter used in a search for ``Shift`` records. ``AND`` logic is used by Square's servers to apply each
    filter property specified.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    sort: Optional[ShiftSort] = UNSET
    """Sets the sort order of search results.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""


class ShiftQueryDict(TypedDict):
    filter: NotRequired[ShiftFilter | ShiftFilterDict]
    sort: NotRequired[ShiftSort | ShiftSortDict]
