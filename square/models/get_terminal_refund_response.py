from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .terminal_refund import TerminalRefund, TerminalRefundDict


class GetTerminalRefundResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    refund: Optional[TerminalRefund] = UNSET
    """Represents a payment refund processed by the Square Terminal. Only supports Interac (Canadian debit network)
    payment refunds."""


class GetTerminalRefundResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    refund: NotRequired[TerminalRefund | TerminalRefundDict]
