from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_created_event_event_context_merge import (
    CustomerCreatedEventEventContextMerge,
    CustomerCreatedEventEventContextMergeDict,
)


class CustomerCreatedEventEventContext(SdkBaseModel):
    """Information about the change that triggered the event."""

    merge: Optional[CustomerCreatedEventEventContextMerge] = UNSET
    """Information about a merge operation, which creates a new customer using aggregated properties from two or more
    existing customers."""


class CustomerCreatedEventEventContextDict(TypedDict):
    merge: NotRequired[CustomerCreatedEventEventContextMergeDict]
