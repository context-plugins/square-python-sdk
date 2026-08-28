from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .transfer_order import TransferOrder, TransferOrderDict


class RetrieveTransferOrderResponse(SdkBaseModel):
    """Response containing the requested transfer order"""

    transfer_order: Optional[TransferOrder] = UNSET
    """Represents a transfer order for moving `CatalogItemVariation <entity:CatalogItemVariation>`__s between `Location
    <entity:Location>`__s. Transfer orders track the entire lifecycle of an inventory transfer, including:
    - What items and quantities are being moved
    - Source and destination locations
    - Current `TransferOrderStatus <entity:TransferOrderStatus>`__
    - Shipping information and tracking
    - Which `TeamMember <entity:TeamMember>`__ initiated the transfer

    This object is commonly used to:
    - Track `CatalogItemVariation <entity:CatalogItemVariation>`__ movements between `Location <entity:Location>`__s
    - Reconcile expected vs received quantities
    - Monitor transfer progress and shipping status
    - Audit inventory movement history"""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request"""


class RetrieveTransferOrderResponseDict(TypedDict):
    transfer_order: NotRequired[TransferOrder | TransferOrderDict]
    errors: NotRequired[list[Error | ErrorDict]]
