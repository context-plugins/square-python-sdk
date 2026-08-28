from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .order import Order, OrderDict
from .order_entry import OrderEntry, OrderEntryDict


class SearchOrdersResponse(SdkBaseModel):
    """Either the ``order_entries`` or ``orders`` field is set, depending on whether ``return_entries`` is set on the
    `SearchOrdersRequest <api-endpoint:Orders-SearchOrders>`__."""

    order_entries: Optional[list[OrderEntry]] = UNSET
    """A list of `OrderEntries <entity:OrderEntry>`__ that fit the query conditions. The list is populated only if
    ``return_entries`` is set to ``true`` in the request."""

    orders: Optional[list[Order]] = UNSET
    """A list of `Order <entity:Order>`__ objects that match the query conditions. The list is populated only if
    ``return_entries`` is set to ``false`` in the request."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If unset, this is the final response. For more
    information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""

    errors: Optional[list[Error]] = UNSET
    """`Errors <entity:Error>`__ encountered during the search."""


class SearchOrdersResponseDict(TypedDict):
    order_entries: NotRequired[list[OrderEntry | OrderEntryDict]]
    orders: NotRequired[list[Order | OrderDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]
