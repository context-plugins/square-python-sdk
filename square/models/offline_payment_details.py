from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OfflinePaymentDetails(SdkBaseModel):
    """Details specific to offline payments."""

    client_created_at: Optional[str] = UNSET
    """The client-side timestamp of when the offline payment was created, in RFC 3339 format."""


class OfflinePaymentDetailsDict(TypedDict):
    client_created_at: NotRequired[str]
