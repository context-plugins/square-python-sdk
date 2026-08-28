from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvoiceFilter(SdkBaseModel):
    """Describes query filters to apply."""

    location_ids: list[str]
    """Limits the search to the specified locations. A location is required. In the current implementation, only one
    location can be specified."""

    customer_ids: Optional[list[str | None]] = UNSET
    """Limits the search to the specified customers, within the specified locations. Specifying a customer is optional.
    In the current implementation, a maximum of one customer can be specified."""


class InvoiceFilterDict(TypedDict):
    location_ids: list[str]
    customer_ids: NotRequired[list[str | None]]
