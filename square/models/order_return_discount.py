from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.order_line_item_discount_scope import OrderLineItemDiscountScopeOrStr
from .enums.order_line_item_discount_type import OrderLineItemDiscountTypeOrStr
from .money import Money, MoneyDict


class OrderReturnDiscount(SdkBaseModel):
    """Represents a discount being returned that applies to one or more return line items in an order.

    Fixed-amount, order-scoped discounts are distributed across all non-zero return line item totals. The amount
    distributed to each return line item is relative to that item’s contribution to the order subtotal."""

    uid: OptionalNullable[str] = UNSET
    """A unique ID that identifies the returned discount only within this order."""

    source_discount_uid: OptionalNullable[str] = UNSET
    """The discount ``uid`` from the order that contains the original application of this discount."""

    catalog_object_id: OptionalNullable[str] = UNSET
    """The catalog object ID referencing `CatalogDiscount <entity:CatalogDiscount>`__."""

    catalog_version: OptionalNullable[int] = UNSET
    """The version of the catalog object that this discount references."""

    name: OptionalNullable[str] = UNSET
    """The discount's name."""

    type_: Optional[OrderLineItemDiscountTypeOrStr] = Field(default=UNSET, alias="type")
    """Indicates how the discount is applied to the associated line item or order."""

    percentage: OptionalNullable[str] = UNSET
    """The percentage of the tax, as a string representation of a decimal number. A value of ``"7.25"`` corresponds to a
    percentage of 7.25%.

    ``percentage`` is not set for amount-based discounts."""

    amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    applied_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    scope: Optional[OrderLineItemDiscountScopeOrStr] = UNSET
    """Indicates whether this is a line-item or order-level discount."""


class OrderReturnDiscountDict(TypedDict):
    uid: NotRequired[str | None]
    source_discount_uid: NotRequired[str | None]
    catalog_object_id: NotRequired[str | None]
    catalog_version: NotRequired[int | None]
    name: NotRequired[str | None]
    type_: NotRequired[OrderLineItemDiscountTypeOrStr]
    percentage: NotRequired[str | None]
    amount_money: NotRequired[Money | MoneyDict]
    applied_money: NotRequired[Money | MoneyDict]
    scope: NotRequired[OrderLineItemDiscountScopeOrStr]
