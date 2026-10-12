from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.gift_card_activity_block_reason import GiftCardActivityBlockReasonOrStr


class GiftCardActivityBlock(SdkBaseModel):
    """Represents details about a ``BLOCK`` `gift card activity type <entity:GiftCardActivityType>`__."""

    reason: GiftCardActivityBlockReasonOrStr
    """Indicates the reason for blocking a `gift card <entity:GiftCard>`__."""


class GiftCardActivityBlockDict(TypedDict):
    reason: GiftCardActivityBlockReasonOrStr
