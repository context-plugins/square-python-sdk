from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CustomerDeletedEventEventContextMerge(SdkBaseModel):
    """Information about a merge operation, which creates a new customer using aggregated properties from two or more
    existing customers."""

    from_customer_ids: Optional[list[str | None]] = UNSET
    """The IDs of the existing customers that were merged and then deleted."""

    to_customer_id: OptionalNullable[str] = UNSET
    """The ID of the new customer created by the merge."""


class CustomerDeletedEventEventContextMergeDict(TypedDict):
    from_customer_ids: NotRequired[list[str | None]]
    to_customer_id: NotRequired[str | None]
