from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.transfer_order_status import TransferOrderStatusOrStr


class TransferOrderFilter(SdkBaseModel):
    """Filter criteria for searching transfer orders"""

    source_location_ids: Optional[list[str | None]] = UNSET
    """Filter by source location IDs"""

    destination_location_ids: Optional[list[str | None]] = UNSET
    """Filter by destination location IDs"""

    statuses: Optional[list[TransferOrderStatusOrStr | None]] = UNSET
    """Filter by order statuses See `TransferOrderStatus <#type-transferorderstatus>`__ for possible values"""


class TransferOrderFilterDict(TypedDict):
    source_location_ids: NotRequired[list[str | None]]
    destination_location_ids: NotRequired[list[str | None]]
    statuses: NotRequired[list[TransferOrderStatusOrStr | None]]
