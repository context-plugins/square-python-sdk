from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class EventMetadata(SdkBaseModel):
    """Contains metadata about a particular `Event <entity:Event>`__."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    api_version: OptionalNullable[str] = UNSET
    """The API version of the event. This corresponds to the default API version of the developer application at the
    time when the event was created."""


class EventMetadataDict(TypedDict):
    event_id: NotRequired[str | None]
    api_version: NotRequired[str | None]
