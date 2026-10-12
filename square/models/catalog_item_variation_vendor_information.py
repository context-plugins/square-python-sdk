from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class CatalogItemVariationVendorInformation(SdkBaseModel):
    """Information about the vendor of an item variation."""

    vendor_id: OptionalNullable[str] = UNSET
    """ID of the `Vendor <entity:Vendor>`__ linked to a default cost of this product. When the product is added to a
    purchase order, the default cost is pre-filled. This field is not validated. Clients should gracefully handle cases
    where the vendor_id does not match any existing vendor."""

    vendor_code: OptionalNullable[str] = UNSET
    """Unique identifier of this product in the specified vendor's' inventory system. When the product is added to a
    purchase order, the vendor code is pre-filled based on the selected vendor."""

    unit_cost_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class CatalogItemVariationVendorInformationDict(TypedDict):
    vendor_id: NotRequired[str | None]
    vendor_code: NotRequired[str | None]
    unit_cost_money: NotRequired[MoneyDict]
