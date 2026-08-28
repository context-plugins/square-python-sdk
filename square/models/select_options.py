from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .select_option import SelectOption, SelectOptionDict


class SelectOptions(SdkBaseModel):
    title: str
    """The title text to display in the select flow on the Terminal."""

    body: str
    """The body text to display in the select flow on the Terminal."""

    options: list[SelectOption]
    """Represents the buttons/options that should be displayed in the select flow on the Terminal."""

    selected_option: Optional[SelectOption] = UNSET


class SelectOptionsDict(TypedDict):
    title: str
    body: str
    options: list[SelectOption | SelectOptionDict]
    selected_option: NotRequired[SelectOption | SelectOptionDict]
