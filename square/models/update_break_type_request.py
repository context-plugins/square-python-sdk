from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .break_type import BreakType, BreakTypeDict


class UpdateBreakTypeRequest(SdkBaseModel):
    """A request to update a ``BreakType``."""

    break_type: BreakType
    """A template for a type of `break <entity:Break>`__ that can be added to a `timecard <entity:Timecard>`__,
    including the expected duration and paid status."""


class UpdateBreakTypeRequestDict(TypedDict):
    break_type: BreakTypeDict
