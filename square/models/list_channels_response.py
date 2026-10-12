from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .channel import Channel, ChannelDict
from .error import Error, ErrorDict


class ListChannelsResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    channels: Optional[list[Channel]] = UNSET
    """List of requested Channel."""

    cursor: Optional[str] = UNSET
    """The token required to retrieve the next page of results."""


class ListChannelsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    channels: NotRequired[list[ChannelDict]]
    cursor: NotRequired[str]
