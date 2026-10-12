from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .order_money_amounts import OrderMoneyAmounts, OrderMoneyAmountsDict
from .order_return_discount import OrderReturnDiscount, OrderReturnDiscountDict
from .order_return_line_item import OrderReturnLineItem, OrderReturnLineItemDict
from .order_return_service_charge import OrderReturnServiceCharge, OrderReturnServiceChargeDict
from .order_return_tax import OrderReturnTax, OrderReturnTaxDict
from .order_return_tip import OrderReturnTip, OrderReturnTipDict
from .order_rounding_adjustment import OrderRoundingAdjustment, OrderRoundingAdjustmentDict


class OrderReturn(SdkBaseModel):
    """The set of line items, service charges, taxes, discounts, tips, and other items being returned in an order."""

    uid: OptionalNullable[str] = UNSET
    """A unique ID that identifies the return only within this order."""

    source_order_id: OptionalNullable[str] = UNSET
    """An order that contains the original sale of these return line items. This is unset for unlinked returns."""

    return_line_items: OptionalNullable[list[OrderReturnLineItem]] = UNSET
    """A collection of line items that are being returned."""

    return_service_charges: OptionalNullable[list[OrderReturnServiceCharge]] = UNSET
    """A collection of service charges that are being returned."""

    return_taxes: OptionalNullable[list[OrderReturnTax]] = UNSET
    """A collection of references to taxes being returned for an order, including the total applied tax amount to be
    returned. The taxes must reference a top-level tax ID from the source order."""

    return_discounts: OptionalNullable[list[OrderReturnDiscount]] = UNSET
    """A collection of references to discounts being returned for an order, including the total applied discount amount
    to be returned. The discounts must reference a top-level discount ID from the source order."""

    return_tips: OptionalNullable[list[OrderReturnTip]] = UNSET
    """A collection of references to tips being returned for an order."""

    rounding_adjustment: Optional[OrderRoundingAdjustment] = UNSET
    """A rounding adjustment of the money being returned. Commonly used to apply cash rounding when the minimum unit of
    the account is smaller than the lowest physical denomination of the currency."""

    return_amounts: Optional[OrderMoneyAmounts] = UNSET
    """A collection of various money amounts."""


class OrderReturnDict(TypedDict):
    uid: NotRequired[str | None]
    source_order_id: NotRequired[str | None]
    return_line_items: NotRequired[list[OrderReturnLineItemDict] | None]
    return_service_charges: NotRequired[list[OrderReturnServiceChargeDict] | None]
    return_taxes: NotRequired[list[OrderReturnTaxDict] | None]
    return_discounts: NotRequired[list[OrderReturnDiscountDict] | None]
    return_tips: NotRequired[list[OrderReturnTipDict] | None]
    rounding_adjustment: NotRequired[OrderRoundingAdjustmentDict]
    return_amounts: NotRequired[OrderMoneyAmountsDict]
