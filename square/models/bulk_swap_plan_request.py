from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BulkSwapPlanRequest(SdkBaseModel):
    """Defines input parameters in a call to the `BulkSwapPlan <api-endpoint:Subscriptions-BulkSwapPlan>`__ endpoint."""

    new_plan_variation_id: str
    """The ID of the new subscription plan variation.

    This field is required."""

    old_plan_variation_id: str
    """The ID of the plan variation whose subscriptions should be swapped. Active subscriptions using this plan
    variation will be subscribed to the new plan variation on their next billing day."""

    location_id: str
    """The ID of the location to associate with the swapped subscriptions."""


class BulkSwapPlanRequestDict(TypedDict):
    new_plan_variation_id: str
    old_plan_variation_id: str
    location_id: str
