from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BreakType(SdkBaseModel):
    """A template for a type of `break <entity:Break>`__ that can be added to a `timecard <entity:Timecard>`__,
    including the expected duration and paid status."""

    id: Optional[str] = UNSET
    """The UUID for this object."""

    location_id: str
    """The ID of the business location this type of break applies to."""

    break_name: str
    """A human-readable name for this type of break. The name is displayed to team members in Square products."""

    expected_duration: str
    """Format: RFC-3339 P[n]Y[n]M[n]DT[n]H[n]M[n]S. The expected length of this break. Precision less than minutes is
    truncated.

    Example for break expected duration of 15 minutes: PT15M"""

    is_paid: bool
    """Whether this break counts towards time worked for compensation purposes."""

    version: Optional[int] = UNSET
    """Used for resolving concurrency issues. The request fails if the version provided does not match the server
    version at the time of the request. If a value is not provided, Square's servers execute a "blind" write;
    potentially overwriting another writer's data."""

    created_at: Optional[str] = UNSET
    """A read-only timestamp in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """A read-only timestamp in RFC 3339 format."""


class BreakTypeDict(TypedDict):
    id: NotRequired[str]
    location_id: str
    break_name: str
    expected_duration: str
    is_paid: bool
    version: NotRequired[int]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
