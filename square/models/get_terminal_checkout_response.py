from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .terminal_checkout import TerminalCheckout, TerminalCheckoutDict


class GetTerminalCheckoutResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    checkout: Optional[TerminalCheckout] = UNSET
    """Represents a checkout processed by the Square Terminal."""


class GetTerminalCheckoutResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    checkout: NotRequired[TerminalCheckout | TerminalCheckoutDict]
