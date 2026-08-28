from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class OrderReturnLineItemModifier(SdkBaseModel):
    """A line item modifier being returned."""

    uid: OptionalNullable[str] = UNSET
    """A unique ID that identifies the return modifier only within this order."""

    source_modifier_uid: OptionalNullable[str] = UNSET
    """The modifier ``uid`` from the order's line item that contains the original sale of this line item modifier."""

    catalog_object_id: OptionalNullable[str] = UNSET
    """The catalog object ID referencing `CatalogModifier <entity:CatalogModifier>`__."""

    catalog_version: OptionalNullable[int] = UNSET
    """The version of the catalog object that this line item modifier references."""

    name: OptionalNullable[str] = UNSET
    """The name of the item modifier."""

    base_price_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    total_price_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    quantity: OptionalNullable[str] = UNSET
    """The quantity of the line item modifier. The modifier quantity can be 0 or more. For example, suppose a restaurant
    offers a cheeseburger on the menu. When a buyer orders this item, the restaurant records the purchase by creating an
    ``Order`` object with a line item for a burger. The line item includes a line item modifier: the name is cheese and
    the quantity is 1. The buyer has the option to order extra cheese (or no cheese). If the buyer chooses the extra
    cheese option, the modifier quantity increases to 2. If the buyer does not want any cheese, the modifier quantity is
    set to 0."""


class OrderReturnLineItemModifierDict(TypedDict):
    uid: NotRequired[str | None]
    source_modifier_uid: NotRequired[str | None]
    catalog_object_id: NotRequired[str | None]
    catalog_version: NotRequired[int | None]
    name: NotRequired[str | None]
    base_price_money: NotRequired[Money | MoneyDict]
    total_price_money: NotRequired[Money | MoneyDict]
    quantity: NotRequired[str | None]
