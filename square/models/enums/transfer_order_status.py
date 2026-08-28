from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferOrderStatus(str, Enum):
    """Status values for transfer orders. Represents the current state of a `TransferOrder <entity:TransferOrder>`__ in
    its lifecycle from creation to completion. Each status determines what actions are available and how inventory is
    affected."""

    DRAFT = "DRAFT"
    """Initial status when transfer order is created via `CreateTransferOrder
    <api-endpoint:TransferOrders-CreateTransferOrder>`__. Order can be modified or deleted. No inventory impact at this
    stage."""

    STARTED = "STARTED"
    """Transfer order has been started via `StartTransferOrder <api-endpoint:TransferOrders-StartTransferOrder>`__.
    Order can no longer be deleted. `CatalogItemVariation <entity:CatalogItemVariation>`__s are decremented from source
    `Location <entity:Location>`__ and marked as in-transit to destination."""

    PARTIALLY_RECEIVED = "PARTIALLY_RECEIVED"
    """Some items have been received via `ReceiveTransferOrder <api-endpoint:TransferOrders-ReceiveTransferOrder>`__ but
    there are still pending quantities. Additional receipts are allowed. `CatalogItemVariation
    <entity:CatalogItemVariation>`__s are incrementally added to destination `Location <entity:Location>`__ inventory as
    they are received."""

    COMPLETED = "COMPLETED"
    """All items have been received or canceled, no pending quantities remain. Only metadata modifications are allowed.
    Final inventory adjustments are complete at both source and destination `Location <entity:Location>`__s."""

    CANCELED = "CANCELED"
    """Transfer order was canceled via `CancelTransferOrder <api-endpoint:TransferOrders-CancelTransferOrder>`__. Any
    pending quantities are no longer receivable and are returned to source `Location <entity:Location>`__. Only metadata
    modifications are allowed."""

    __str__ = str.__str__


TransferOrderStatusOrStr: TypeAlias = Annotated[TransferOrderStatus | str, open_enum_validator(TransferOrderStatus)]
