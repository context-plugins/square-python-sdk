from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .event import Event, EventDict
from .event_metadata import EventMetadata, EventMetadataDict


class SearchEventsResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `SearchEvents
    <api-endpoint:Events-SearchEvents>`__ endpoint.

    Note: if there are errors processing the request, the events field will not be present."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    events: Optional[list[Event]] = UNSET
    """The list of `Event <entity:Event>`__s returned by the search."""

    metadata: Optional[list[EventMetadata]] = UNSET
    """Contains the metadata of an event. For more information, see `Event <entity:Event>`__."""

    cursor: Optional[str] = UNSET
    """When a response is truncated, it includes a cursor that you can use in a subsequent request to fetch the next set
    of events. If empty, this is the final response.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class SearchEventsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    events: NotRequired[list[EventDict]]
    metadata: NotRequired[list[EventMetadataDict]]
    cursor: NotRequired[str]
