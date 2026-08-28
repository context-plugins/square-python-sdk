from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TransferOrderLine(SdkBaseModel):
    """Represents a line item in a transfer order. Each line item tracks a specific `CatalogItemVariation
    <entity:CatalogItemVariation>`__ being transferred, including ordered quantities and receipt status."""

    uid: Optional[str] = UNSET
    """Unique system-generated identifier for the line item. Provide when updating/removing a line via
    `UpdateTransferOrder <api-endpoint:TransferOrders-UpdateTransferOrder>`__."""

    item_variation_id: str
    """The required identifier of the `CatalogItemVariation <entity:CatalogItemVariation>`__ being transferred. Must
    reference a valid catalog item variation that exists in the `Catalog <api:Catalog>`__."""

    quantity_ordered: str
    """Total quantity ordered, formatted as a decimal string (e.g. "10 or 10.0000"). Required to be a positive number.

    To remove a line item, set ``remove`` to ``true`` in `UpdateTransferOrder
    <api-endpoint:TransferOrders-UpdateTransferOrder>`__."""

    quantity_pending: Optional[str] = UNSET
    """Calculated quantity of this line item's yet to be received stock. This is the difference between the total
    quantity ordered and the sum of quantities received, canceled, and damaged."""

    quantity_received: Optional[str] = UNSET
    """Quantity received at destination. These items are added to the destination `Location <entity:Location>`__'s
    inventory with `InventoryState <entity:InventoryState>`__ of IN_STOCK.

    This field cannot be updated directly in Create/Update operations, instead use `ReceiveTransferOrder
    <api-endpoint:TransferOrders-ReceiveTransferOrder>`__."""

    quantity_damaged: Optional[str] = UNSET
    """Quantity received in damaged condition. These items are added to the destination `Location <entity:Location>`__'s
    inventory with `InventoryState <entity:InventoryState>`__ of WASTE.

    This field cannot be updated directly in Create/Update operations, instead use `ReceiveTransferOrder
    <api-endpoint:TransferOrders-ReceiveTransferOrder>`__."""

    quantity_canceled: Optional[str] = UNSET
    """Quantity that was canceled. These items will be immediately added to inventory in the source location.

    This field cannot be updated directly in Create/Update operations, instead use `ReceiveTransferOrder
    <api-endpoint:TransferOrders-ReceiveTransferOrder>`__ or `CancelTransferOrder
    <api-endpoint:TransferOrders-CancelTransferOrder>`__."""


class TransferOrderLineDict(TypedDict):
    uid: NotRequired[str]
    item_variation_id: str
    quantity_ordered: str
    quantity_pending: NotRequired[str]
    quantity_received: NotRequired[str]
    quantity_damaged: NotRequired[str]
    quantity_canceled: NotRequired[str]
