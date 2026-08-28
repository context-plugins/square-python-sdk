from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order_line_item_pricing_blocklists_blocked_discount import (
    OrderLineItemPricingBlocklistsBlockedDiscount,
    OrderLineItemPricingBlocklistsBlockedDiscountDict,
)
from .order_line_item_pricing_blocklists_blocked_service_charge import (
    OrderLineItemPricingBlocklistsBlockedServiceCharge,
    OrderLineItemPricingBlocklistsBlockedServiceChargeDict,
)
from .order_line_item_pricing_blocklists_blocked_tax import (
    OrderLineItemPricingBlocklistsBlockedTax,
    OrderLineItemPricingBlocklistsBlockedTaxDict,
)


class OrderLineItemPricingBlocklists(SdkBaseModel):
    """Describes pricing adjustments that are blocked from automatic application to a line item. For more information,
    see `Apply Taxes and Discounts <https://developer.squareup.com/docs/orders-api/apply-taxes-and-discounts>`__."""

    blocked_discounts: Optional[list[OrderLineItemPricingBlocklistsBlockedDiscount | None]] = UNSET
    """A list of discounts blocked from applying to the line item. Discounts can be blocked by the ``discount_uid`` (for
    ad hoc discounts) or the ``discount_catalog_object_id`` (for catalog discounts)."""

    blocked_taxes: Optional[list[OrderLineItemPricingBlocklistsBlockedTax | None]] = UNSET
    """A list of taxes blocked from applying to the line item. Taxes can be blocked by the ``tax_uid`` (for ad hoc
    taxes) or the ``tax_catalog_object_id`` (for catalog taxes)."""

    blocked_service_charges: Optional[list[OrderLineItemPricingBlocklistsBlockedServiceCharge | None]] = UNSET
    """A list of service charges blocked from applying to the line item. Service charges can be blocked by the
    ``service_charge_uid`` (for ad hoc service charges) or the ``service_charge_catalog_object_id`` (for catalog service
    charges)."""


class OrderLineItemPricingBlocklistsDict(TypedDict):
    blocked_discounts: NotRequired[
        list[OrderLineItemPricingBlocklistsBlockedDiscount | OrderLineItemPricingBlocklistsBlockedDiscountDict | None]
    ]
    blocked_taxes: NotRequired[
        list[OrderLineItemPricingBlocklistsBlockedTax | OrderLineItemPricingBlocklistsBlockedTaxDict | None]
    ]
    blocked_service_charges: NotRequired[
        list[
            (
                OrderLineItemPricingBlocklistsBlockedServiceCharge
                | OrderLineItemPricingBlocklistsBlockedServiceChargeDict
                | None
            )
        ]
    ]
