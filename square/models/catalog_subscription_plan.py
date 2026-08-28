from __future__ import annotations

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .subscription_phase import SubscriptionPhase, SubscriptionPhaseDict

if TYPE_CHECKING:
    from .catalog_object import CatalogObject, CatalogObjectDict


class CatalogSubscriptionPlan(SdkBaseModel):
    """Describes a subscription plan. A subscription plan represents what you want to sell in a subscription model, and
    includes references to each of the associated subscription plan variations. For more information, see `Subscription
    Plans and Variations <https://developer.squareup.com/docs/subscriptions-api/plans-and-variations>`__."""

    name: str
    """The name of the plan."""

    phases: Optional[list[SubscriptionPhase | None]] = UNSET
    """A list of SubscriptionPhase containing the `SubscriptionPhase <entity:SubscriptionPhase>`__ for this plan. This
    field it required. Not including this field will throw a REQUIRED_FIELD_MISSING error"""

    subscription_plan_variations: Optional[list[CatalogObject | None]] = UNSET
    """The list of subscription plan variations available for this product"""

    eligible_item_ids: Optional[list[str | None]] = UNSET
    """The list of IDs of ``CatalogItems`` that are eligible for subscription by this SubscriptionPlan's variations."""

    eligible_category_ids: Optional[list[str | None]] = UNSET
    """The list of IDs of ``CatalogCategory`` that are eligible for subscription by this SubscriptionPlan's
    variations."""

    all_items: OptionalNullable[bool] = UNSET
    """If true, all items in the merchant's catalog are subscribable by this SubscriptionPlan."""


class CatalogSubscriptionPlanDict(TypedDict):
    name: str
    phases: NotRequired[list[SubscriptionPhase | SubscriptionPhaseDict | None]]
    subscription_plan_variations: NotRequired[list[CatalogObject | CatalogObjectDict | None]]
    eligible_item_ids: NotRequired[list[str | None]]
    eligible_category_ids: NotRequired[list[str | None]]
    all_items: NotRequired[bool | None]
