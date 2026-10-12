from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_checkout_query_filter import TerminalCheckoutQueryFilter, TerminalCheckoutQueryFilterDict
from .terminal_checkout_query_sort import TerminalCheckoutQuerySort, TerminalCheckoutQuerySortDict


class TerminalCheckoutQuery(SdkBaseModel):
    filter: Optional[TerminalCheckoutQueryFilter] = UNSET
    sort: Optional[TerminalCheckoutQuerySort] = UNSET


class TerminalCheckoutQueryDict(TypedDict):
    filter: NotRequired[TerminalCheckoutQueryFilterDict]
    sort: NotRequired[TerminalCheckoutQuerySortDict]
