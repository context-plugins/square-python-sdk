from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SearchOrdersCustomerFilter(SdkBaseModel):
    """A filter based on the order ``customer_id`` and any tender ``customer_id`` associated with the order. It does not
    filter based on the `FulfillmentRecipient <entity:FulfillmentRecipient>`__ ``customer_id``."""

    customer_ids: Optional[list[str | None]] = UNSET
    """A list of customer IDs to filter by.

    Max: 10 customer ids."""


class SearchOrdersCustomerFilterDict(TypedDict):
    customer_ids: NotRequired[list[str | None]]
