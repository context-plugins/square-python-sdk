from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_transfer_order_data import CreateTransferOrderData, CreateTransferOrderDataDict


class CreateTransferOrderRequest(SdkBaseModel):
    """Request to create a new transfer order."""

    idempotency_key: str
    """A unique string that identifies this CreateTransferOrder request. Keys can be any valid string but must be unique
    for every CreateTransferOrder request."""

    transfer_order: CreateTransferOrderData
    """Data for creating a new transfer order to move `CatalogItemVariation <entity:CatalogItemVariation>`__s between
    `Location <entity:Location>`__s. Used with the `CreateTransferOrder
    <api-endpoint:TransferOrders-CreateTransferOrder>`__ endpoint."""


class CreateTransferOrderRequestDict(TypedDict):
    idempotency_key: str
    transfer_order: CreateTransferOrderDataDict
