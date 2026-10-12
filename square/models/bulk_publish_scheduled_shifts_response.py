from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .publish_scheduled_shift_response import PublishScheduledShiftResponse, PublishScheduledShiftResponseDict


class BulkPublishScheduledShiftsResponse(SdkBaseModel):
    """Represents a `BulkPublishScheduledShifts <api-endpoint:Labor-BulkPublishScheduledShifts>`__ response. Either
    ``scheduled_shifts`` or ``errors`` is present in the response."""

    responses: Optional[dict[str, PublishScheduledShiftResponse]] = UNSET
    """A map of key-value pairs that represent responses for individual publish requests. The order of responses might
    differ from the order in which the requests were provided.

    - Each key is the scheduled shift ID that was specified for a publish request.
    - Each value is the corresponding response. If the request succeeds, the value is the
    published scheduled shift. If the request fails, the value is an ``errors`` array containing any errors that
    occurred while processing the request."""

    errors: Optional[list[Error]] = UNSET
    """Any top-level errors that prevented the bulk operation from succeeding."""


class BulkPublishScheduledShiftsResponseDict(TypedDict):
    responses: NotRequired[dict[str, PublishScheduledShiftResponseDict]]
    errors: NotRequired[list[ErrorDict]]
