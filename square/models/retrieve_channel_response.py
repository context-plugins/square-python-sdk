from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .channel import Channel, ChannelDict
from .error import Error, ErrorDict


class RetrieveChannelResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    channel: Optional[Channel] = UNSET


class RetrieveChannelResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    channel: NotRequired[Channel | ChannelDict]
