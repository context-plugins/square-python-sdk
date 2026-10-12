from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .subscription_phase import SubscriptionPhase, SubscriptionPhaseDict


class CatalogSubscriptionPlanVariation(SdkBaseModel):
    """Describes a subscription plan variation. A subscription plan variation represents how the subscription for a
    product or service is sold. For more information, see `Subscription Plans and Variations
    <https://developer.squareup.com/docs/subscriptions-api/plans-and-variations>`__."""

    name: str
    """The name of the plan variation."""

    phases: list[SubscriptionPhase]
    """A list containing each `SubscriptionPhase <entity:SubscriptionPhase>`__ for this plan variation."""

    subscription_plan_id: OptionalNullable[str] = UNSET
    """The id of the subscription plan, if there is one."""

    monthly_billing_anchor_date: OptionalNullable[int] = UNSET
    """The day of the month the billing period starts."""

    can_prorate: OptionalNullable[bool] = UNSET
    """Whether bills for this plan variation can be split for proration."""

    successor_plan_variation_id: OptionalNullable[str] = UNSET
    """The ID of a "successor" plan variation to this one. If the field is set, and this object is disabled at all
    locations, it indicates that this variation is deprecated and the object identified by the successor ID be used in
    its stead."""


class CatalogSubscriptionPlanVariationDict(TypedDict):
    name: str
    phases: list[SubscriptionPhaseDict]
    subscription_plan_id: NotRequired[str | None]
    monthly_billing_anchor_date: NotRequired[int | None]
    can_prorate: NotRequired[bool | None]
    successor_plan_variation_id: NotRequired[str | None]
