from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .gift_card_customer_linked_event_object import (
    GiftCardCustomerLinkedEventObject,
    GiftCardCustomerLinkedEventObjectDict,
)


class GiftCardCustomerLinkedEventData(SdkBaseModel):
    """The data associated with a ``gift_card.customer_linked`` event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``gift_card``."""

    id: Optional[str] = UNSET
    """The ID of the updated gift card."""

    object_: Optional[GiftCardCustomerLinkedEventObject] = Field(default=UNSET, alias="object")
    """An object that contains the gift card and customer ID associated with a ``gift_card.customer_linked`` event."""


class GiftCardCustomerLinkedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[GiftCardCustomerLinkedEventObjectDict]
