from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_refund_query_filter import TerminalRefundQueryFilter, TerminalRefundQueryFilterDict
from .terminal_refund_query_sort import TerminalRefundQuerySort, TerminalRefundQuerySortDict


class TerminalRefundQuery(SdkBaseModel):
    filter: Optional[TerminalRefundQueryFilter] = UNSET
    sort: Optional[TerminalRefundQuerySort] = UNSET


class TerminalRefundQueryDict(TypedDict):
    filter: NotRequired[TerminalRefundQueryFilter | TerminalRefundQueryFilterDict]
    sort: NotRequired[TerminalRefundQuerySort | TerminalRefundQuerySortDict]
