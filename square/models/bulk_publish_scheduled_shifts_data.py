from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BulkPublishScheduledShiftsData(SdkBaseModel):
    """Represents options for an individual publish request in a `BulkPublishScheduledShifts
    <api-endpoint:Labor-BulkPublishScheduledShifts>`__ operation, provided as the value in a key-value pair."""

    version: Optional[int] = UNSET
    """The current version of the scheduled shift, used to enable `optimistic concurrency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__ control. If the
    provided version doesn't match the server version, the request fails. If omitted, Square executes a blind write,
    potentially overwriting data from another publish request."""


class BulkPublishScheduledShiftsDataDict(TypedDict):
    version: NotRequired[int]
