from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.subscription_event_info_code import SubscriptionEventInfoCodeOrStr


class SubscriptionEventInfo(SdkBaseModel):
    """Provides information about the subscription event."""

    detail: OptionalNullable[str] = UNSET
    """A human-readable explanation for the event."""

    code: Optional[SubscriptionEventInfoCodeOrStr] = UNSET
    """Supported info codes of a subscription event."""


class SubscriptionEventInfoDict(TypedDict):
    detail: NotRequired[str | None]
    code: NotRequired[SubscriptionEventInfoCodeOrStr]
