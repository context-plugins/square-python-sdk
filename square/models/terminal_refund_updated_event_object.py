from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_refund import TerminalRefund, TerminalRefundDict


class TerminalRefundUpdatedEventObject(SdkBaseModel):
    refund: Optional[TerminalRefund] = UNSET
    """Represents a payment refund processed by the Square Terminal. Only supports Interac (Canadian debit network)
    payment refunds."""


class TerminalRefundUpdatedEventObjectDict(TypedDict):
    refund: NotRequired[TerminalRefundDict]
