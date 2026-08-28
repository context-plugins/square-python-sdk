from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .terminal_checkout import TerminalCheckout, TerminalCheckoutDict


class CreateTerminalCheckoutRequest(SdkBaseModel):
    idempotency_key: str
    """A unique string that identifies this ``CreateCheckout`` request. Keys can be any valid string but must be unique
    for every ``CreateCheckout`` request.

    See `Idempotency keys <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__ for more
    information."""

    checkout: TerminalCheckout
    """Represents a checkout processed by the Square Terminal."""


class CreateTerminalCheckoutRequestDict(TypedDict):
    idempotency_key: str
    checkout: TerminalCheckout | TerminalCheckoutDict
