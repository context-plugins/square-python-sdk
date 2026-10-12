from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .terminal_refund import TerminalRefund, TerminalRefundDict


class DismissTerminalRefundResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    refund: Optional[TerminalRefund] = UNSET
    """Represents a payment refund processed by the Square Terminal. Only supports Interac (Canadian debit network)
    payment refunds."""


class DismissTerminalRefundResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    refund: NotRequired[TerminalRefundDict]
