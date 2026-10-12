from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .card_automatically_updated_event_data import (
    CardAutomaticallyUpdatedEventData,
    CardAutomaticallyUpdatedEventDataDict,
)


class CardAutomaticallyUpdatedEvent(SdkBaseModel):
    """Published when Square automatically updates the expiration date or primary account number (PAN) of a `card
    <entity:Card>`__ or adds or removes an issuer alert."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target seller associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of this event. The value is ``"card.automatically_updated"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[CardAutomaticallyUpdatedEventData] = UNSET


class CardAutomaticallyUpdatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[CardAutomaticallyUpdatedEventDataDict]
