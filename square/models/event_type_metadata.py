from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EventTypeMetadata(SdkBaseModel):
    """Contains the metadata of a webhook event type."""

    event_type: Optional[str] = UNSET
    """The event type."""

    api_version_introduced: Optional[str] = UNSET
    """The API version at which the event type was introduced."""

    release_status: Optional[str] = UNSET
    """The release status of the event type."""


class EventTypeMetadataDict(TypedDict):
    event_type: NotRequired[str]
    api_version_introduced: NotRequired[str]
    release_status: NotRequired[str]
