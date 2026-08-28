from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class BreakModel(SdkBaseModel):
    """A record of a team member's break on a `timecard <entity:Timecard>`__."""

    id: Optional[str] = UNSET
    """The UUID for this object."""

    start_at: str
    """RFC 3339; follows the same timezone information as the `timecard <entity:Timecard>`__. Precision up to the minute
    is respected; seconds are truncated."""

    end_at: OptionalNullable[str] = UNSET
    """RFC 3339; follows the same timezone information as the `timecard <entity:Timecard>`__. Precision up to the minute
    is respected; seconds are truncated."""

    break_type_id: str
    """The `BreakType <entity:BreakType>`__ that this break was templated on."""

    name: str
    """A human-readable name."""

    expected_duration: str
    """Format: RFC-3339 P[n]Y[n]M[n]DT[n]H[n]M[n]S. The expected length of the break.

    Example for break expected duration of 15 minutes: PT15M"""

    is_paid: bool
    """Whether this break counts towards time worked for compensation purposes."""


class BreakModelDict(TypedDict):
    id: NotRequired[str]
    start_at: str
    end_at: NotRequired[str | None]
    break_type_id: str
    name: str
    expected_duration: str
    is_paid: bool
