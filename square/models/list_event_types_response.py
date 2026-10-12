from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .event_type_metadata import EventTypeMetadata, EventTypeMetadataDict


class ListEventTypesResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `ListEventTypes
    <api-endpoint:Events-ListEventTypes>`__ endpoint.

    Note: if there are errors processing the request, the event types field will not be present."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    event_types: Optional[list[str]] = UNSET
    """The list of event types."""

    metadata: Optional[list[EventTypeMetadata]] = UNSET
    """Contains the metadata of an event type. For more information, see `EventTypeMetadata
    <entity:EventTypeMetadata>`__."""


class ListEventTypesResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    event_types: NotRequired[list[str]]
    metadata: NotRequired[list[EventTypeMetadataDict]]
