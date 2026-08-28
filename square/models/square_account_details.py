from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .error import Error, ErrorDict


class SquareAccountDetails(SdkBaseModel):
    """Additional details about Square Account payments."""

    payment_source_token: OptionalNullable[str] = UNSET
    """Unique identifier for the payment source used for this payment."""

    errors: Optional[list[Error | None]] = UNSET
    """Information about errors encountered during the request."""


class SquareAccountDetailsDict(TypedDict):
    payment_source_token: NotRequired[str | None]
    errors: NotRequired[list[Error | ErrorDict | None]]
