from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.order_line_item_tax_scope import OrderLineItemTaxScopeOrStr
from .enums.order_line_item_tax_type import OrderLineItemTaxTypeOrStr
from .money import Money, MoneyDict


class OrderReturnTax(SdkBaseModel):
    """Represents a tax being returned that applies to one or more return line items in an order.

    Fixed-amount, order-scoped taxes are distributed across all non-zero return line item totals. The amount distributed
    to each return line item is relative to that item’s contribution to the order subtotal."""

    uid: OptionalNullable[str] = UNSET
    """A unique ID that identifies the returned tax only within this order."""

    source_tax_uid: OptionalNullable[str] = UNSET
    """The tax ``uid`` from the order that contains the original tax charge."""

    catalog_object_id: OptionalNullable[str] = UNSET
    """The catalog object ID referencing `CatalogTax <entity:CatalogTax>`__."""

    catalog_version: OptionalNullable[int] = UNSET
    """The version of the catalog object that this tax references."""

    name: OptionalNullable[str] = UNSET
    """The tax's name."""

    type_: Optional[OrderLineItemTaxTypeOrStr] = Field(default=UNSET, alias="type")
    """Indicates how the tax is applied to the associated line item or order."""

    percentage: OptionalNullable[str] = UNSET
    """The percentage of the tax, as a string representation of a decimal number. For example, a value of ``"7.25"``
    corresponds to a percentage of 7.25%."""

    applied_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    scope: Optional[OrderLineItemTaxScopeOrStr] = UNSET
    """Indicates whether this is a line-item or order-level tax."""


class OrderReturnTaxDict(TypedDict):
    uid: NotRequired[str | None]
    source_tax_uid: NotRequired[str | None]
    catalog_object_id: NotRequired[str | None]
    catalog_version: NotRequired[int | None]
    name: NotRequired[str | None]
    type_: NotRequired[OrderLineItemTaxTypeOrStr]
    percentage: NotRequired[str | None]
    applied_money: NotRequired[Money | MoneyDict]
    scope: NotRequired[OrderLineItemTaxScopeOrStr]
