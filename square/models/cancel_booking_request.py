from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CancelBookingRequest(SdkBaseModel):
    idempotency_key: OptionalNullable[str] = UNSET
    """A unique key to make this request an idempotent operation."""

    booking_version: OptionalNullable[int] = UNSET
    """The revision number for the booking used for optimistic concurrency."""


class CancelBookingRequestDict(TypedDict):
    idempotency_key: NotRequired[str | None]
    booking_version: NotRequired[int | None]
