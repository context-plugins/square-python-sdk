from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class StartTransferOrderRequest(SdkBaseModel):
    """Request to start a transfer order, changing its status from DRAFT to STARTED."""

    idempotency_key: str
    """A unique string that identifies this UpdateTransferOrder request. Keys can be any valid string but must be unique
    for every UpdateTransferOrder request."""

    version: Optional[int] = UNSET
    """Version for optimistic concurrency"""


class StartTransferOrderRequestDict(TypedDict):
    idempotency_key: str
    version: NotRequired[int]
