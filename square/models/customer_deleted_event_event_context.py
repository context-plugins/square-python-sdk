from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_deleted_event_event_context_merge import (
    CustomerDeletedEventEventContextMerge,
    CustomerDeletedEventEventContextMergeDict,
)


class CustomerDeletedEventEventContext(SdkBaseModel):
    """Information about the change that triggered the event."""

    merge: Optional[CustomerDeletedEventEventContextMerge] = UNSET
    """Information about a merge operation, which creates a new customer using aggregated properties from two or more
    existing customers."""


class CustomerDeletedEventEventContextDict(TypedDict):
    merge: NotRequired[CustomerDeletedEventEventContextMergeDict]
