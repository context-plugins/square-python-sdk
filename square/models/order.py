from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.order_state import OrderStateOrStr
from .fulfillment import Fulfillment, FulfillmentDict
from .money import Money, MoneyDict
from .order_line_item import OrderLineItem, OrderLineItemDict
from .order_line_item_discount import OrderLineItemDiscount, OrderLineItemDiscountDict
from .order_line_item_tax import OrderLineItemTax, OrderLineItemTaxDict
from .order_money_amounts import OrderMoneyAmounts, OrderMoneyAmountsDict
from .order_pricing_options import OrderPricingOptions, OrderPricingOptionsDict
from .order_return import OrderReturn, OrderReturnDict
from .order_reward import OrderReward, OrderRewardDict
from .order_rounding_adjustment import OrderRoundingAdjustment, OrderRoundingAdjustmentDict
from .order_service_charge import OrderServiceCharge, OrderServiceChargeDict
from .order_source import OrderSource, OrderSourceDict
from .refund import Refund, RefundDict
from .tender import Tender, TenderDict


class Order(SdkBaseModel):
    """Contains all information related to a single order to process with Square, including line items that specify the
    products to purchase. ``Order`` objects also include information about any associated tenders, refunds, and returns.

    All Connect V2 Transactions have all been converted to Orders including all associated itemization data."""

    id: Optional[str] = UNSET
    """The order's unique ID."""

    location_id: str
    """The ID of the seller location that this order is associated with."""

    reference_id: OptionalNullable[str] = UNSET
    """A client-specified ID to associate an entity in another system with this order."""

    source: Optional[OrderSource] = UNSET
    """Represents the origination details of an order."""

    customer_id: OptionalNullable[str] = UNSET
    """The ID of the `customer <entity:Customer>`__ associated with the order.

    You should specify a ``customer_id`` on the order (or the payment) to ensure that transactions are reliably linked
    to customers. Omitting this field might result in the creation of new `instant profiles
    <https://developer.squareup.com/docs/customers-api/what-it-does#instant-profiles>`__."""

    line_items: Optional[list[OrderLineItem | None]] = UNSET
    """The line items included in the order."""

    taxes: Optional[list[OrderLineItemTax | None]] = UNSET
    """The list of all taxes associated with the order.

    Taxes can be scoped to either ``ORDER`` or ``LINE_ITEM``. For taxes with ``LINE_ITEM`` scope, an
    ``OrderLineItemAppliedTax`` must be added to each line item that the tax applies to. For taxes with ``ORDER`` scope,
    the server generates an ``OrderLineItemAppliedTax`` for every line item.

    On reads, each tax in the list includes the total amount of that tax applied to the order.

    __IMPORTANT__: If ``LINE_ITEM`` scope is set on any taxes in this field, using the deprecated ``line_items.taxes``
    field results in an error. Use ``line_items.applied_taxes`` instead."""

    discounts: Optional[list[OrderLineItemDiscount | None]] = UNSET
    """The list of all discounts associated with the order.

    Discounts can be scoped to either ``ORDER`` or ``LINE_ITEM``. For discounts scoped to ``LINE_ITEM``, an
    ``OrderLineItemAppliedDiscount`` must be added to each line item that the discount applies to. For discounts with
    ``ORDER`` scope, the server generates an ``OrderLineItemAppliedDiscount`` for every line item.

    __IMPORTANT__: If ``LINE_ITEM`` scope is set on any discounts in this field, using the deprecated
    ``line_items.discounts`` field results in an error. Use ``line_items.applied_discounts`` instead."""

    service_charges: Optional[list[OrderServiceCharge | None]] = UNSET
    """A list of service charges applied to the order."""

    fulfillments: Optional[list[Fulfillment | None]] = UNSET
    """Details about order fulfillment.

    Orders can only be created with at most one fulfillment. However, orders returned by the API might contain multiple
    fulfillments."""

    returns: Optional[list[OrderReturn]] = UNSET
    """A collection of items from sale orders being returned in this one. Normally part of an itemized return or
    exchange. There is exactly one ``Return`` object per sale ``Order`` being referenced."""

    return_amounts: Optional[OrderMoneyAmounts] = UNSET
    """A collection of various money amounts."""

    net_amounts: Optional[OrderMoneyAmounts] = UNSET
    """A collection of various money amounts."""

    rounding_adjustment: Optional[OrderRoundingAdjustment] = UNSET
    """A rounding adjustment of the money being returned. Commonly used to apply cash rounding when the minimum unit of
    the account is smaller than the lowest physical denomination of the currency."""

    tenders: Optional[list[Tender]] = UNSET
    """The tenders that were used to pay for the order."""

    refunds: Optional[list[Refund]] = UNSET
    """The refunds that are part of this order."""

    metadata: Optional[dict[str, str | None]] = UNSET
    """Application-defined data attached to this order. Metadata fields are intended to store descriptive references or
    associations with an entity in another system or store brief information about the object. Square does not process
    this field; it only stores and returns it in relevant API calls. Do not use metadata to store any sensitive
    information (such as personally identifiable information or card details).

    Keys written by applications must be 60 characters or less and must be in the character set ``[a-zA-Z0-9_-]``.
    Entries can also include metadata generated by Square. These keys are prefixed with a namespace, separated from the
    key with a ':' character.

    Values have a maximum length of 255 characters.

    An application can have up to 10 entries per metadata field.

    Entries written by applications are private and can only be read or modified by the same application.

    For more information, see `Metadata <https://developer.squareup.com/docs/build-basics/metadata>`__."""

    created_at: Optional[str] = UNSET
    """The timestamp for when the order was created, at server side, in RFC 3339 format (for example,
    "2016-09-04T23:59:33.123Z")."""

    updated_at: Optional[str] = UNSET
    """The timestamp for when the order was last updated, at server side, in RFC 3339 format (for example,
    "2016-09-04T23:59:33.123Z")."""

    closed_at: Optional[str] = UNSET
    """The timestamp for when the order reached a terminal `state <entity:OrderState>`__, in RFC 3339 format (for
    example "2016-09-04T23:59:33.123Z")."""

    state: Optional[OrderStateOrStr] = UNSET
    """The state of the order."""

    version: Optional[int] = UNSET
    """The version number, which is incremented each time an update is committed to the order. Orders not created
    through the API do not include a version number and therefore cannot be updated.

    `Read more about working with versions
    <https://developer.squareup.com/docs/orders-api/manage-orders/update-orders>`__."""

    total_money: Optional[Money] = UNSET
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

    total_tip_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    total_service_charge_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    ticket_name: OptionalNullable[str] = UNSET
    """A short-term identifier for the order (such as a customer first name, table number, or auto-generated order
    number that resets daily)."""

    pricing_options: Optional[OrderPricingOptions] = UNSET
    """Pricing options for an order. The options affect how the order's price is calculated. They can be used, for
    example, to apply automatic price adjustments that are based on preconfigured `pricing rules
    <entity:CatalogPricingRule>`__."""

    rewards: Optional[list[OrderReward]] = UNSET
    """A set-like list of Rewards that have been added to the Order."""

    net_amount_due_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class OrderDict(TypedDict):
    id: NotRequired[str]
    location_id: str
    reference_id: NotRequired[str | None]
    source: NotRequired[OrderSource | OrderSourceDict]
    customer_id: NotRequired[str | None]
    line_items: NotRequired[list[OrderLineItem | OrderLineItemDict | None]]
    taxes: NotRequired[list[OrderLineItemTax | OrderLineItemTaxDict | None]]
    discounts: NotRequired[list[OrderLineItemDiscount | OrderLineItemDiscountDict | None]]
    service_charges: NotRequired[list[OrderServiceCharge | OrderServiceChargeDict | None]]
    fulfillments: NotRequired[list[Fulfillment | FulfillmentDict | None]]
    returns: NotRequired[list[OrderReturn | OrderReturnDict]]
    return_amounts: NotRequired[OrderMoneyAmounts | OrderMoneyAmountsDict]
    net_amounts: NotRequired[OrderMoneyAmounts | OrderMoneyAmountsDict]
    rounding_adjustment: NotRequired[OrderRoundingAdjustment | OrderRoundingAdjustmentDict]
    tenders: NotRequired[list[Tender | TenderDict]]
    refunds: NotRequired[list[Refund | RefundDict]]
    metadata: NotRequired[dict[str, str | None]]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    closed_at: NotRequired[str]
    state: NotRequired[OrderStateOrStr]
    version: NotRequired[int]
    total_money: NotRequired[Money | MoneyDict]
    total_tax_money: NotRequired[Money | MoneyDict]
    total_discount_money: NotRequired[Money | MoneyDict]
    total_tip_money: NotRequired[Money | MoneyDict]
    total_service_charge_money: NotRequired[Money | MoneyDict]
    ticket_name: NotRequired[str | None]
    pricing_options: NotRequired[OrderPricingOptions | OrderPricingOptionsDict]
    rewards: NotRequired[list[OrderReward | OrderRewardDict]]
    net_amount_due_money: NotRequired[Money | MoneyDict]
