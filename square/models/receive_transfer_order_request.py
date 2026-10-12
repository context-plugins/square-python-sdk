from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .transfer_order_goods_receipt import TransferOrderGoodsReceipt, TransferOrderGoodsReceiptDict


class ReceiveTransferOrderRequest(SdkBaseModel):
    """Request to record receipt of items for a transfer order"""

    idempotency_key: str
    """A unique key to make this request idempotent"""

    receipt: TransferOrderGoodsReceipt
    """The goods receipt details for a transfer order. This object represents a single receipt of goods against a
    transfer order, tracking:

    - Which `CatalogItemVariation <entity:CatalogItemVariation>`__s were received
    - Quantities received in good condition
    - Quantities damaged during transit/handling
    - Quantities canceled during receipt

    Multiple goods receipts can be created for a single transfer order to handle:
    - Partial deliveries
    - Multiple shipments
    - Split receipts across different dates
    - Cancellations of specific quantities

    Each receipt automatically:
    - Updates the transfer order status
    - Adjusts received quantities
    - Updates inventory levels at both source and destination `Location <entity:Location>`__s"""

    version: Optional[int] = UNSET
    """Version for optimistic concurrency"""


class ReceiveTransferOrderRequestDict(TypedDict):
    idempotency_key: str
    receipt: TransferOrderGoodsReceiptDict
    version: NotRequired[int]
