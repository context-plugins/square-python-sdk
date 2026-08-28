from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.inventory_state import InventoryStateOrStr


class BatchRetrieveInventoryCountsRequest(SdkBaseModel):
    catalog_object_ids: Optional[list[str | None]] = UNSET
    """The filter to return results by ``CatalogObject`` ID. The filter is applicable only when set. The default is
    null."""

    location_ids: Optional[list[str | None]] = UNSET
    """The filter to return results by ``Location`` ID. This filter is applicable only when set. The default is null."""

    updated_after: OptionalNullable[str] = UNSET
    """The filter to return results with their ``calculated_at`` value after the given time as specified in an RFC 3339
    timestamp. The default value is the UNIX epoch of (``1970-01-01T00:00:00Z``)."""

    cursor: OptionalNullable[str] = UNSET
    """A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of
    results for the original query.

    See the `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more
    information."""

    states: Optional[list[InventoryStateOrStr | None]] = UNSET
    """The filter to return results by ``InventoryState``. The filter is only applicable when set. Ignored are untracked
    states of ``NONE``, ``SOLD``, and ``UNLINKED_RETURN``. The default is null."""

    limit: OptionalNullable[int] = UNSET
    """The number of `records <entity:InventoryCount>`__ to return."""


class BatchRetrieveInventoryCountsRequestDict(TypedDict):
    catalog_object_ids: NotRequired[list[str | None]]
    location_ids: NotRequired[list[str | None]]
    updated_after: NotRequired[str | None]
    cursor: NotRequired[str | None]
    states: NotRequired[list[InventoryStateOrStr | None]]
    limit: NotRequired[int | None]
