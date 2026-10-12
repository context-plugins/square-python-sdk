from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .catalog_object import CatalogObject, CatalogObjectDict
from .order import Order, OrderDict


class PaymentLinkRelatedResources(SdkBaseModel):
    orders: OptionalNullable[list[Order]] = UNSET
    """The order associated with the payment link."""

    subscription_plans: OptionalNullable[list[CatalogObject]] = UNSET
    """The subscription plan associated with the payment link."""


class PaymentLinkRelatedResourcesDict(TypedDict):
    orders: NotRequired[list[OrderDict] | None]
    subscription_plans: NotRequired[list[CatalogObjectDict] | None]
