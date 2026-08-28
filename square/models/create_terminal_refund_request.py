from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_refund import TerminalRefund, TerminalRefundDict


class CreateTerminalRefundRequest(SdkBaseModel):
    idempotency_key: str
    """A unique string that identifies this ``CreateRefund`` request. Keys can be any valid string but must be unique
    for every ``CreateRefund`` request.

    See `Idempotency keys <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__ for more
    information."""

    refund: Optional[TerminalRefund] = UNSET
    """Represents a payment refund processed by the Square Terminal. Only supports Interac (Canadian debit network)
    payment refunds."""


class CreateTerminalRefundRequestDict(TypedDict):
    idempotency_key: str
    refund: NotRequired[TerminalRefund | TerminalRefundDict]
