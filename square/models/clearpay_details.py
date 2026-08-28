from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ClearpayDetails(SdkBaseModel):
    """Additional details about Clearpay payments."""

    email_address: OptionalNullable[str] = UNSET
    """Email address on the buyer's Clearpay account."""


class ClearpayDetailsDict(TypedDict):
    email_address: NotRequired[str | None]
