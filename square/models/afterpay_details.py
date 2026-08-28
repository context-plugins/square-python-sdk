from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class AfterpayDetails(SdkBaseModel):
    """Additional details about Afterpay payments."""

    email_address: OptionalNullable[str] = UNSET
    """Email address on the buyer's Afterpay account."""


class AfterpayDetailsDict(TypedDict):
    email_address: NotRequired[str | None]
