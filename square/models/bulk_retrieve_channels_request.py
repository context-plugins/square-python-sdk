from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BulkRetrieveChannelsRequest(SdkBaseModel):
    """Defines the fields that are included in the request body for the `BulkRetrieveChannels
    <api-endpoint:Channels-BulkRetrieveChannels>`__ endpoint."""

    channel_ids: list[str]


class BulkRetrieveChannelsRequestDict(TypedDict):
    channel_ids: list[str]
