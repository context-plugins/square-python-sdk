from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .update_transfer_order_data import UpdateTransferOrderData, UpdateTransferOrderDataDict


class UpdateTransferOrderRequest(SdkBaseModel):
    """Request to update a transfer order"""

    idempotency_key: str
    """A unique string that identifies this UpdateTransferOrder request. Keys must contain only alphanumeric characters,
    dashes and underscores"""

    transfer_order: UpdateTransferOrderData
    """Data model for updating a transfer order. All fields are optional."""

    version: Optional[int] = UNSET
    """Version for optimistic concurrency"""


class UpdateTransferOrderRequestDict(TypedDict):
    idempotency_key: str
    transfer_order: UpdateTransferOrderDataDict
    version: NotRequired[int]
