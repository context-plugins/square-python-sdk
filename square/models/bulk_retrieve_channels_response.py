from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .retrieve_channel_response import RetrieveChannelResponse, RetrieveChannelResponseDict


class BulkRetrieveChannelsResponse(SdkBaseModel):
    """Defines the fields that are included in the request body for the `BulkRetrieveChannels
    <api-endpoint:Channels-BulkRetrieveChannels>`__ endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    responses: Optional[dict[str, RetrieveChannelResponse]] = UNSET
    """A map of channel IDs to channel responses which tell whether retrieval for a specific channel is success or not.
    Channel response of a success retrieval would contain channel info whereas channel response of a failed retrieval
    would have error info."""


class BulkRetrieveChannelsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    responses: NotRequired[dict[str, RetrieveChannelResponse | RetrieveChannelResponseDict]]
