from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_action_query_filter import TerminalActionQueryFilter, TerminalActionQueryFilterDict
from .terminal_action_query_sort import TerminalActionQuerySort, TerminalActionQuerySortDict


class TerminalActionQuery(SdkBaseModel):
    filter: Optional[TerminalActionQueryFilter] = UNSET
    sort: Optional[TerminalActionQuerySort] = UNSET


class TerminalActionQueryDict(TypedDict):
    filter: NotRequired[TerminalActionQueryFilterDict]
    sort: NotRequired[TerminalActionQuerySortDict]
