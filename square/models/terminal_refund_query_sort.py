from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TerminalRefundQuerySort(SdkBaseModel):
    sort_order: OptionalNullable[str] = UNSET
    """The order in which results are listed.
    - ``ASC`` - Oldest to newest.
    - ``DESC`` - Newest to oldest (default)."""


class TerminalRefundQuerySortDict(TypedDict):
    sort_order: NotRequired[str | None]
