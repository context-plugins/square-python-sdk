from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .gift_card import GiftCard, GiftCardDict


class CreateGiftCardRequest(SdkBaseModel):
    """Represents a `CreateGiftCard <api-endpoint:GiftCards-CreateGiftCard>`__ request."""

    idempotency_key: str
    """A unique identifier for this request, used to ensure idempotency. For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""

    location_id: str
    """The ID of the `location <entity:Location>`__ where the gift card should be registered for reporting purposes.
    Gift cards can be redeemed at any of the seller's locations."""

    gift_card: GiftCard
    """Represents a Square gift card."""


class CreateGiftCardRequestDict(TypedDict):
    idempotency_key: str
    location_id: str
    gift_card: GiftCardDict
