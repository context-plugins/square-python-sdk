from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .time_range import TimeRange, TimeRangeDict


class TerminalCheckoutQueryFilter(SdkBaseModel):
    device_id: OptionalNullable[str] = UNSET
    """The ``TerminalCheckout`` objects associated with a specific device. If no device is specified, then all
    ``TerminalCheckout`` objects for the merchant are displayed."""

    created_at: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    status: OptionalNullable[str] = UNSET
    """Filtered results with the desired status of the ``TerminalCheckout``. Options: ``PENDING``, ``IN_PROGRESS``,
    ``CANCEL_REQUESTED``, ``CANCELED``, ``COMPLETED``"""


class TerminalCheckoutQueryFilterDict(TypedDict):
    device_id: NotRequired[str | None]
    created_at: NotRequired[TimeRangeDict]
    status: NotRequired[str | None]
