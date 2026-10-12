from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dispute import Dispute, DisputeDict


class DisputeStateChangedEventObject(SdkBaseModel):
    object_: Optional[Dispute] = Field(default=UNSET, alias="object")
    """Represents a `dispute <https://developer.squareup.com/docs/disputes-api/overview>`__ a cardholder initiated with
    their bank."""


class DisputeStateChangedEventObjectDict(TypedDict):
    object_: NotRequired[DisputeDict]
