from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SearchOrdersSourceFilter(SdkBaseModel):
    """A filter based on order ``source`` information."""

    source_names: Optional[list[str | None]] = UNSET
    """Filters by the `Source <entity:OrderSource>`__ ``name``. The filter returns any orders with a ``source.name``
    that matches any of the listed source names.

    Max: 10 source names."""


class SearchOrdersSourceFilterDict(TypedDict):
    source_names: NotRequired[list[str | None]]
