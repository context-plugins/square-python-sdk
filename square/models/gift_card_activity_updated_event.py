from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .gift_card_activity_updated_event_data import (
    GiftCardActivityUpdatedEventData,
    GiftCardActivityUpdatedEventDataDict,
)


class GiftCardActivityUpdatedEvent(SdkBaseModel):
    """Published when a `gift card activity <entity:GiftCardActivity>`__ is updated. Subscribe to this event to be
    notified about the following changes:
    - An update to the ``REDEEM`` activity for a gift card redemption made from a Square product (such as Square Point
        of Sale).
    These redemptions are initially assigned a ``PENDING`` state, but then change to a ``COMPLETED`` or ``CANCELED``
    state.
    - An update to the ``IMPORT`` activity for an imported gift card when the balance is later adjusted by Square."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the Square seller associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event. For this event, the value is ``gift_card.activity.updated``."""

    event_id: OptionalNullable[str] = UNSET
    """The unique ID of the event, which is used for `idempotency support
    <https://developer.squareup.com/docs/webhooks/step4manage#webhooks-best-practices>`__."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[GiftCardActivityUpdatedEventData] = UNSET
    """The data associated with a ``gift_card.activity.updated`` event."""


class GiftCardActivityUpdatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[GiftCardActivityUpdatedEventData | GiftCardActivityUpdatedEventDataDict]
