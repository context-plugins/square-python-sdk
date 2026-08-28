from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .terminal_action import TerminalAction, TerminalActionDict


class CreateTerminalActionRequest(SdkBaseModel):
    idempotency_key: str
    """A unique string that identifies this ``CreateAction`` request. Keys can be any valid string but must be unique
    for every ``CreateAction`` request.

    See `Idempotency keys <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__ for more
    information."""

    action: TerminalAction
    """Represents an action processed by the Square Terminal."""


class CreateTerminalActionRequestDict(TypedDict):
    idempotency_key: str
    action: TerminalAction | TerminalActionDict
