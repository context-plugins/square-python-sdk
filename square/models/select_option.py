from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SelectOption(SdkBaseModel):
    reference_id: str
    """The reference id for the option."""

    title: str
    """The title text that displays in the select option button."""


class SelectOptionDict(TypedDict):
    reference_id: str
    title: str
