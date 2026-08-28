from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExcludeStrategy(str, Enum):
    """Indicates which products matched by a CatalogPricingRule will be excluded if the pricing rule uses an exclude
    set."""

    LEAST_EXPENSIVE = "LEAST_EXPENSIVE"
    """The least expensive matched products are excluded from the pricing. If the pricing rule is set to exclude one
    product and multiple products in the match set qualify as least expensive, then one will be excluded at random.

    Excluding the least expensive product gives the best discount value to the buyer."""

    MOST_EXPENSIVE = "MOST_EXPENSIVE"
    """The most expensive matched product is excluded from the pricing rule. If multiple products have the same price
    and all qualify as least expensive, one will be excluded at random.

    This guarantees that the most expensive product is purchased at full price."""

    MOST_EXPENSIVE_LOWEST_VALUE = "MOST_EXPENSIVE_LOWEST_VALUE"
    """Like MOST_EXPENSIVE, the most expensive matched product is excluded and purchased at full price. However, instead
    of maximizing the discount value on the remaining products (standard BOGO), the discount is applied to the CHEAPEST
    remaining eligible product.

    Used by the "lowest-value free item" coupon shape where the intent is to make the least expensive item free, not the
    most valuable one."""

    __str__ = str.__str__


ExcludeStrategyOrStr: TypeAlias = Annotated[ExcludeStrategy | str, open_enum_validator(ExcludeStrategy)]
