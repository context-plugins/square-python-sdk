from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_checkout import TerminalCheckout, TerminalCheckoutDict


class TerminalCheckoutUpdatedEventObject(SdkBaseModel):
    checkout: Optional[TerminalCheckout] = UNSET
    """Represents a checkout processed by the Square Terminal."""


class TerminalCheckoutUpdatedEventObjectDict(TypedDict):
    checkout: NotRequired[TerminalCheckoutDict]
