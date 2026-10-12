from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.terminal_action_action_type import TerminalActionActionTypeOrStr
from .time_range import TimeRange, TimeRangeDict


class TerminalActionQueryFilter(SdkBaseModel):
    device_id: OptionalNullable[str] = UNSET
    """``TerminalAction``s associated with a specific device. If no device is specified then all ``TerminalAction``s for
    the merchant will be displayed."""

    created_at: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    status: OptionalNullable[str] = UNSET
    """Filter results with the desired status of the ``TerminalAction`` Options: ``PENDING``, ``IN_PROGRESS``,
    ``CANCEL_REQUESTED``, ``CANCELED``, ``COMPLETED``"""

    type_: Optional[TerminalActionActionTypeOrStr] = Field(default=UNSET, alias="type")
    """Describes the type of this unit and indicates which field contains the unit information. This is an ‘open’
    enum."""


class TerminalActionQueryFilterDict(TypedDict):
    device_id: NotRequired[str | None]
    created_at: NotRequired[TimeRangeDict]
    status: NotRequired[str | None]
    type_: NotRequired[TerminalActionActionTypeOrStr]
