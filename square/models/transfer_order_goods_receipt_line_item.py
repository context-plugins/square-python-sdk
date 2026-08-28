from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TransferOrderGoodsReceiptLineItem(SdkBaseModel):
    """A simplified line item for goods receipts in transfer orders"""

    transfer_order_line_uid: str
    """The unique identifier of the Transfer Order line being received"""

    quantity_received: OptionalNullable[str] = UNSET
    """The quantity received for this line item as a decimal string (e.g. "10.5"). These items will be added to the
    destination `Location <entity:Location>`__'s inventory with `InventoryState <entity:InventoryState>`__ of
    IN_STOCK."""

    quantity_damaged: OptionalNullable[str] = UNSET
    """The quantity that was damaged during shipping/handling as a decimal string (e.g. "1.5"). These items will be
    added to the destination `Location <entity:Location>`__'s inventory with `InventoryState <entity:InventoryState>`__
    of WASTE."""

    quantity_canceled: OptionalNullable[str] = UNSET
    """The quantity that was canceled during shipping/handling as a decimal string (e.g. "1.5"). These will be
    immediately added to inventory in the source location."""


class TransferOrderGoodsReceiptLineItemDict(TypedDict):
    transfer_order_line_uid: str
    quantity_received: NotRequired[str | None]
    quantity_damaged: NotRequired[str | None]
    quantity_canceled: NotRequired[str | None]
