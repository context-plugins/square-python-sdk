from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CardPaymentTimeline(SdkBaseModel):
    """The timeline for card payments."""

    authorized_at: OptionalNullable[str] = UNSET
    """The timestamp when the payment was authorized, in RFC 3339 format."""

    captured_at: OptionalNullable[str] = UNSET
    """The timestamp when the payment was captured, in RFC 3339 format."""

    voided_at: OptionalNullable[str] = UNSET
    """The timestamp when the payment was voided, in RFC 3339 format."""


class CardPaymentTimelineDict(TypedDict):
    authorized_at: NotRequired[str | None]
    captured_at: NotRequired[str | None]
    voided_at: NotRequired[str | None]
