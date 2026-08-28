from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConfirmationDecision(SdkBaseModel):
    has_agreed: Optional[bool] = UNSET
    """The buyer's decision to the displayed terms."""


class ConfirmationDecisionDict(TypedDict):
    has_agreed: NotRequired[bool]
