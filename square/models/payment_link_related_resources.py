from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_object import CatalogObject, CatalogObjectDict
from .order import Order, OrderDict


class PaymentLinkRelatedResources(SdkBaseModel):
    orders: Optional[list[Order | None]] = UNSET
    """The order associated with the payment link."""

    subscription_plans: Optional[list[CatalogObject | None]] = UNSET
    """The subscription plan associated with the payment link."""


class PaymentLinkRelatedResourcesDict(TypedDict):
    orders: NotRequired[list[Order | OrderDict | None]]
    subscription_plans: NotRequired[list[CatalogObject | CatalogObjectDict | None]]
