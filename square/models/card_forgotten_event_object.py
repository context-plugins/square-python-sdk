from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card_forgotten_event_card import CardForgottenEventCard, CardForgottenEventCardDict


class CardForgottenEventObject(SdkBaseModel):
    card: Optional[CardForgottenEventCard] = UNSET


class CardForgottenEventObjectDict(TypedDict):
    card: NotRequired[CardForgottenEventCardDict]
