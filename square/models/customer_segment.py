from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CustomerSegment(SdkBaseModel):
    """Represents a group of customer profiles that match one or more predefined filter criteria.

    Segments (also known as Smart Groups) are defined and created within the Customer Directory in the Square Seller
    Dashboard or Point of Sale."""

    id: Optional[str] = UNSET
    """A unique Square-generated ID for the segment."""

    name: str
    """The name of the segment."""

    created_at: Optional[str] = UNSET
    """The timestamp when the segment was created, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp when the segment was last updated, in RFC 3339 format."""


class CustomerSegmentDict(TypedDict):
    id: NotRequired[str]
    name: str
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
