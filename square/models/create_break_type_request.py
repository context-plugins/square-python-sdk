from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .break_type import BreakType, BreakTypeDict


class CreateBreakTypeRequest(SdkBaseModel):
    """A request to create a new ``BreakType``."""

    idempotency_key: Optional[str] = UNSET
    """A unique string value to ensure the idempotency of the operation."""

    break_type: BreakType
    """A template for a type of `break <entity:Break>`__ that can be added to a `timecard <entity:Timecard>`__,
    including the expected duration and paid status."""


class CreateBreakTypeRequestDict(TypedDict):
    idempotency_key: NotRequired[str]
    break_type: BreakType | BreakTypeDict
