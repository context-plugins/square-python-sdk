from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .gift_card import GiftCard, GiftCardDict


class GiftCardCustomerUnlinkedEventObject(SdkBaseModel):
    """An object that contains the gift card and the customer ID associated with a ``gift_card.customer_linked``
    event."""

    gift_card: Optional[GiftCard] = UNSET
    """Represents a Square gift card."""

    unlinked_customer_id: OptionalNullable[str] = UNSET
    """The ID of the unlinked `customer <entity:Customer>`__."""


class GiftCardCustomerUnlinkedEventObjectDict(TypedDict):
    gift_card: NotRequired[GiftCard | GiftCardDict]
    unlinked_customer_id: NotRequired[str | None]
