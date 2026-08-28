from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreateTransferOrderLineData(SdkBaseModel):
    """Data for creating a new transfer order line item. Each line item specifies a `CatalogItemVariation
    <entity:CatalogItemVariation>`__ and quantity to transfer."""

    item_variation_id: str
    """ID of the `CatalogItemVariation <entity:CatalogItemVariation>`__ to transfer. Must reference a valid item
    variation in the `Catalog <api:Catalog>`__. The item variation must be:
    - Active and available for sale
    - Enabled for inventory tracking
    - Available at the source location"""

    quantity_ordered: str
    """Total quantity ordered"""


class CreateTransferOrderLineDataDict(TypedDict):
    item_variation_id: str
    quantity_ordered: str
