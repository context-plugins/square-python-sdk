from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.destination_type import DestinationTypeOrStr


class Destination(SdkBaseModel):
    """Information about the destination against which the payout was made."""

    type_: Optional[DestinationTypeOrStr] = Field(default=UNSET, alias="type")
    """List of possible destinations against which a payout can be made."""

    id: Optional[str] = UNSET
    """Square issued unique ID (also known as the instrument ID) associated with this destination."""


class DestinationDict(TypedDict):
    type_: NotRequired[DestinationTypeOrStr]
    id: NotRequired[str]
