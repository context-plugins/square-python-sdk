from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .confirmation_decision import ConfirmationDecision, ConfirmationDecisionDict


class ConfirmationOptions(SdkBaseModel):
    title: str
    """The title text to display in the confirmation screen flow on the Terminal."""

    body: str
    """The agreement details to display in the confirmation flow on the Terminal."""

    agree_button_text: str
    """The button text to display indicating the customer agrees to the displayed terms."""

    disagree_button_text: OptionalNullable[str] = UNSET
    """The button text to display indicating the customer does not agree to the displayed terms."""

    decision: Optional[ConfirmationDecision] = UNSET


class ConfirmationOptionsDict(TypedDict):
    title: str
    body: str
    agree_button_text: str
    disagree_button_text: NotRequired[str | None]
    decision: NotRequired[ConfirmationDecisionDict]
