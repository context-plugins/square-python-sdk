from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.order_line_item_item_type import OrderLineItemItemTypeOrStr
from .money import Money, MoneyDict
from .order_line_item_applied_discount import OrderLineItemAppliedDiscount, OrderLineItemAppliedDiscountDict
from .order_line_item_applied_service_charge import (
    OrderLineItemAppliedServiceCharge,
    OrderLineItemAppliedServiceChargeDict,
)
from .order_line_item_applied_tax import OrderLineItemAppliedTax, OrderLineItemAppliedTaxDict
from .order_quantity_unit import OrderQuantityUnit, OrderQuantityUnitDict
from .order_return_line_item_modifier import OrderReturnLineItemModifier, OrderReturnLineItemModifierDict


class OrderReturnLineItem(SdkBaseModel):
    """The line item being returned in an order."""

    uid: OptionalNullable[str] = UNSET
    """A unique ID for this return line-item entry."""

    source_line_item_uid: OptionalNullable[str] = UNSET
    """The ``uid`` of the line item in the original sale order."""

    name: OptionalNullable[str] = UNSET
    """The name of the line item."""

    quantity: str
    """The quantity returned, formatted as a decimal number. For example, ``"3"``.

    Line items with a ``quantity_unit`` can have non-integer quantities. For example, ``"1.70000"``."""

    quantity_unit: Optional[OrderQuantityUnit] = UNSET
    """Contains the measurement unit for a quantity and a precision that specifies the number of digits after the
    decimal point for decimal quantities."""

    note: OptionalNullable[str] = UNSET
    """The note of the return line item."""

    catalog_object_id: OptionalNullable[str] = UNSET
    """The `CatalogItemVariation <entity:CatalogItemVariation>`__ ID applied to this return line item."""

    catalog_version: OptionalNullable[int] = UNSET
    """The version of the catalog object that this line item references."""

    variation_name: OptionalNullable[str] = UNSET
    """The name of the variation applied to this return line item."""

    item_type: Optional[OrderLineItemItemTypeOrStr] = UNSET
    """Represents the line item type."""

    return_modifiers: Optional[list[OrderReturnLineItemModifier | None]] = UNSET
    """The `CatalogModifier <entity:CatalogModifier>`__s applied to this line item."""

    applied_taxes: Optional[list[OrderLineItemAppliedTax | None]] = UNSET
    """The list of references to ``OrderReturnTax`` entities applied to the return line item. Each
    ``OrderLineItemAppliedTax`` has a ``tax_uid`` that references the ``uid`` of a top-level ``OrderReturnTax`` applied
    to the return line item. On reads, the applied amount is populated."""

    applied_discounts: Optional[list[OrderLineItemAppliedDiscount | None]] = UNSET
    """The list of references to ``OrderReturnDiscount`` entities applied to the return line item. Each
    ``OrderLineItemAppliedDiscount`` has a ``discount_uid`` that references the ``uid`` of a top-level
    ``OrderReturnDiscount`` applied to the return line item. On reads, the applied amount is populated."""

    base_price_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    variation_total_price_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    gross_return_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    total_tax_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    total_discount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    total_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    applied_service_charges: Optional[list[OrderLineItemAppliedServiceCharge | None]] = UNSET
    """The list of references to ``OrderReturnServiceCharge`` entities applied to the return line item. Each
    ``OrderLineItemAppliedServiceCharge`` has a ``service_charge_uid`` that references the ``uid`` of a top-level
    ``OrderReturnServiceCharge`` applied to the return line item. On reads, the applied amount is populated."""

    total_service_charge_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class OrderReturnLineItemDict(TypedDict):
    uid: NotRequired[str | None]
    source_line_item_uid: NotRequired[str | None]
    name: NotRequired[str | None]
    quantity: str
    quantity_unit: NotRequired[OrderQuantityUnit | OrderQuantityUnitDict]
    note: NotRequired[str | None]
    catalog_object_id: NotRequired[str | None]
    catalog_version: NotRequired[int | None]
    variation_name: NotRequired[str | None]
    item_type: NotRequired[OrderLineItemItemTypeOrStr]
    return_modifiers: NotRequired[list[OrderReturnLineItemModifier | OrderReturnLineItemModifierDict | None]]
    applied_taxes: NotRequired[list[OrderLineItemAppliedTax | OrderLineItemAppliedTaxDict | None]]
    applied_discounts: NotRequired[list[OrderLineItemAppliedDiscount | OrderLineItemAppliedDiscountDict | None]]
    base_price_money: NotRequired[Money | MoneyDict]
    variation_total_price_money: NotRequired[Money | MoneyDict]
    gross_return_money: NotRequired[Money | MoneyDict]
    total_tax_money: NotRequired[Money | MoneyDict]
    total_discount_money: NotRequired[Money | MoneyDict]
    total_money: NotRequired[Money | MoneyDict]
    applied_service_charges: NotRequired[
        list[OrderLineItemAppliedServiceCharge | OrderLineItemAppliedServiceChargeDict | None]
    ]
    total_service_charge_money: NotRequired[Money | MoneyDict]
