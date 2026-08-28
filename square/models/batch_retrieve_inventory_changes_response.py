from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .inventory_change import InventoryChange, InventoryChangeDict


class BatchRetrieveInventoryChangesResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    changes: Optional[list[InventoryChange]] = UNSET
    """The current calculated inventory changes for the requested objects and locations."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If unset, this is the final response. See the
    `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more information."""


class BatchRetrieveInventoryChangesResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    changes: NotRequired[list[InventoryChange | InventoryChangeDict]]
    cursor: NotRequired[str]
