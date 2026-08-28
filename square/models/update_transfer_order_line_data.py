from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class UpdateTransferOrderLineData(SdkBaseModel):
    """Represents a line item update in a transfer order"""

    uid: OptionalNullable[str] = UNSET
    """Line item id being updated. Required for updating/removing existing line items, but should not be set for new
    line items."""

    item_variation_id: OptionalNullable[str] = UNSET
    """Catalog item variation being transferred

    Required for new line items, but otherwise is not updatable."""

    quantity_ordered: OptionalNullable[str] = UNSET
    """Total quantity ordered"""

    remove: OptionalNullable[bool] = UNSET
    """Flag to remove the line item during update. Must include ``uid`` in removal request"""


class UpdateTransferOrderLineDataDict(TypedDict):
    uid: NotRequired[str | None]
    item_variation_id: NotRequired[str | None]
    quantity_ordered: NotRequired[str | None]
    remove: NotRequired[bool | None]
