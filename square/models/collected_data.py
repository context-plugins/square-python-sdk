from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CollectedData(SdkBaseModel):
    input_text: Optional[str] = UNSET
    """The buyer's input text."""


class CollectedDataDict(TypedDict):
    input_text: NotRequired[str]
