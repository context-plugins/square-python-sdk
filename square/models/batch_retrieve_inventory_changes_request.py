from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .batch_retrieve_inventory_changes_sort import (
    BatchRetrieveInventoryChangesSort,
    BatchRetrieveInventoryChangesSortDict,
)
from .enums.inventory_change_type import InventoryChangeTypeOrStr
from .enums.inventory_state import InventoryStateOrStr
from .inventory_adjustment_reason_id import InventoryAdjustmentReasonId, InventoryAdjustmentReasonIdDict


class BatchRetrieveInventoryChangesRequest(SdkBaseModel):
    catalog_object_ids: Optional[list[str | None]] = UNSET
    """The filter to return results by ``CatalogObject`` ID. The filter is only applicable when set. The default value
    is null."""

    location_ids: Optional[list[str | None]] = UNSET
    """The filter to return results by ``Location`` ID. The filter is only applicable when set. The default value is
    null."""

    types: Optional[list[InventoryChangeTypeOrStr | None]] = UNSET
    """The filter to return results by ``InventoryChangeType`` values other than ``TRANSFER``. The default value is
    ``[PHYSICAL_COUNT, ADJUSTMENT]``."""

    states: Optional[list[InventoryStateOrStr | None]] = UNSET
    """The filter to return ``ADJUSTMENT`` query results by ``InventoryState``. This filter is only applied when set.
    The default value is null."""

    updated_after: OptionalNullable[str] = UNSET
    """The filter to return results with their ``calculated_at`` value after the given time as specified in an RFC 3339
    timestamp. The default value is the UNIX epoch of (``1970-01-01T00:00:00Z``)."""

    updated_before: OptionalNullable[str] = UNSET
    """The filter to return results with their ``created_at`` or ``calculated_at`` value strictly before the given time
    as specified in an RFC 3339 timestamp. The default value is the UNIX epoch of (``1970-01-01T00:00:00Z``)."""

    cursor: OptionalNullable[str] = UNSET
    """A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of
    results for the original query.

    See the `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more
    information."""

    limit: OptionalNullable[int] = UNSET
    """The number of `records <entity:InventoryChange>`__ to return."""

    sort: Optional[BatchRetrieveInventoryChangesSort] = UNSET
    reason_ids: Optional[list[InventoryAdjustmentReasonId | None]] = UNSET
    """The filter to return ``ADJUSTMENT`` query results by inventory adjustment reason. This filter is only applied
    when set. The request cannot include both ``reason_ids`` and ``states``."""


class BatchRetrieveInventoryChangesRequestDict(TypedDict):
    catalog_object_ids: NotRequired[list[str | None]]
    location_ids: NotRequired[list[str | None]]
    types: NotRequired[list[InventoryChangeTypeOrStr | None]]
    states: NotRequired[list[InventoryStateOrStr | None]]
    updated_after: NotRequired[str | None]
    updated_before: NotRequired[str | None]
    cursor: NotRequired[str | None]
    limit: NotRequired[int | None]
    sort: NotRequired[BatchRetrieveInventoryChangesSort | BatchRetrieveInventoryChangesSortDict]
    reason_ids: NotRequired[list[InventoryAdjustmentReasonId | InventoryAdjustmentReasonIdDict | None]]
