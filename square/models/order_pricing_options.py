from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class OrderPricingOptions(SdkBaseModel):
    """Pricing options for an order. The options affect how the order's price is calculated. They can be used, for
    example, to apply automatic price adjustments that are based on preconfigured `pricing rules
    <entity:CatalogPricingRule>`__."""

    auto_apply_discounts: OptionalNullable[bool] = UNSET
    """The option to determine whether pricing rule-based discounts are automatically applied to an order."""

    auto_apply_taxes: OptionalNullable[bool] = UNSET
    """The option to determine whether rule-based taxes are automatically applied to an order when the criteria of the
    corresponding rules are met."""


class OrderPricingOptionsDict(TypedDict):
    auto_apply_discounts: NotRequired[bool | None]
    auto_apply_taxes: NotRequired[bool | None]
