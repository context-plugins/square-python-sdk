from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .inventory_count import InventoryCount, InventoryCountDict


class RetrieveInventoryCountResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    counts: Optional[list[InventoryCount]] = UNSET
    """The current calculated inventory counts for the requested object and locations."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If unset, this is the final response.

    See the `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more
    information."""


class RetrieveInventoryCountResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    counts: NotRequired[list[InventoryCountDict]]
    cursor: NotRequired[str]
