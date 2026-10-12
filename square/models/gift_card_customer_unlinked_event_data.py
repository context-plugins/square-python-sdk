from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .gift_card_customer_unlinked_event_object import (
    GiftCardCustomerUnlinkedEventObject,
    GiftCardCustomerUnlinkedEventObjectDict,
)


class GiftCardCustomerUnlinkedEventData(SdkBaseModel):
    """The data associated with a ``gift_card.customer_unlinked`` event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``gift_card``."""

    id: Optional[str] = UNSET
    """The ID of the updated gift card."""

    object_: Optional[GiftCardCustomerUnlinkedEventObject] = Field(default=UNSET, alias="object")
    """An object that contains the gift card and the customer ID associated with a ``gift_card.customer_linked``
    event."""


class GiftCardCustomerUnlinkedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[GiftCardCustomerUnlinkedEventObjectDict]
