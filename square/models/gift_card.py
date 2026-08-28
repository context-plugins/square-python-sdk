from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.gift_card_gansource import GiftCardGansourceOrStr
from .enums.gift_card_status import GiftCardStatusOrStr
from .enums.gift_card_type import GiftCardTypeOrStr
from .money import Money, MoneyDict


class GiftCard(SdkBaseModel):
    """Represents a Square gift card."""

    id: Optional[str] = UNSET
    """The Square-assigned ID of the gift card."""

    type_: GiftCardTypeOrStr = Field(alias="type")
    """Indicates the gift card type."""

    gan_source: Optional[GiftCardGansourceOrStr] = UNSET
    """Indicates the source that generated the gift card account number (GAN)."""

    state: Optional[GiftCardStatusOrStr] = UNSET
    """Indicates the gift card state."""

    balance_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    gan: OptionalNullable[str] = UNSET
    """The gift card account number (GAN). Buyers can use the GAN to make purchases or check the gift card balance."""

    created_at: Optional[str] = UNSET
    """The timestamp when the gift card was created, in RFC 3339 format. In the case of a digital gift card, it is the
    time when you create a card (using the Square Point of Sale application, Seller Dashboard, or Gift Cards API). In
    the case of a plastic gift card, it is the time when Square associates the card with the seller at the time of
    activation."""

    customer_ids: Optional[list[str]] = UNSET
    """The IDs of the `customer profiles <entity:Customer>`__ to whom this gift card is linked."""


class GiftCardDict(TypedDict):
    id: NotRequired[str]
    type_: GiftCardTypeOrStr
    gan_source: NotRequired[GiftCardGansourceOrStr]
    state: NotRequired[GiftCardStatusOrStr]
    balance_money: NotRequired[Money | MoneyDict]
    gan: NotRequired[str | None]
    created_at: NotRequired[str]
    customer_ids: NotRequired[list[str]]
