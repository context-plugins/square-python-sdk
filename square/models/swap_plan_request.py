from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .phase_input import PhaseInput, PhaseInputDict


class SwapPlanRequest(SdkBaseModel):
    """Defines input parameters in a call to the `SwapPlan <api-endpoint:Subscriptions-SwapPlan>`__ endpoint."""

    new_plan_variation_id: OptionalNullable[str] = UNSET
    """The ID of the new subscription plan variation.

    This field is required."""

    phases: OptionalNullable[list[PhaseInput]] = UNSET
    """A list of PhaseInputs, to pass phase-specific information used in the swap."""


class SwapPlanRequestDict(TypedDict):
    new_plan_variation_id: NotRequired[str | None]
    phases: NotRequired[list[PhaseInputDict] | None]
