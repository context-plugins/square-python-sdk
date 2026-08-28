from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .gift_card_customer_unlinked_event_data import (
    GiftCardCustomerUnlinkedEventData,
    GiftCardCustomerUnlinkedEventDataDict,
)


class GiftCardCustomerUnlinkedEvent(SdkBaseModel):
    """Published when a `customer <entity:Customer>`__ is unlinked from a `gift card <entity:GiftCard>`__."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the Square seller associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event. For this event, the value is ``gift_card.customer_unlinked``."""

    event_id: OptionalNullable[str] = UNSET
    """The unique ID of the event, which is used for `idempotency support
    <https://developer.squareup.com/docs/webhooks/step4manage#webhooks-best-practices>`__."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[GiftCardCustomerUnlinkedEventData] = UNSET
    """The data associated with a ``gift_card.customer_unlinked`` event."""


class GiftCardCustomerUnlinkedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[GiftCardCustomerUnlinkedEventData | GiftCardCustomerUnlinkedEventDataDict]
