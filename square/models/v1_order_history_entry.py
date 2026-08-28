from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.v1_order_history_entry_action import V1OrderHistoryEntryActionOrStr


class V1OrderHistoryEntry(SdkBaseModel):
    """V1OrderHistoryEntry"""

    action: Optional[V1OrderHistoryEntryActionOrStr] = UNSET
    created_at: Optional[str] = UNSET
    """The time when the action was performed, in ISO 8601 format."""


class V1OrderHistoryEntryDict(TypedDict):
    action: NotRequired[V1OrderHistoryEntryActionOrStr]
    created_at: NotRequired[str]
