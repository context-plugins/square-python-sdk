from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .gift_card import GiftCard, GiftCardDict


class GiftCardCustomerLinkedEventObject(SdkBaseModel):
    """An object that contains the gift card and customer ID associated with a ``gift_card.customer_linked`` event."""

    gift_card: Optional[GiftCard] = UNSET
    """Represents a Square gift card."""

    linked_customer_id: OptionalNullable[str] = UNSET
    """The ID of the linked `customer <entity:Customer>`__."""


class GiftCardCustomerLinkedEventObjectDict(TypedDict):
    gift_card: NotRequired[GiftCardDict]
    linked_customer_id: NotRequired[str | None]
