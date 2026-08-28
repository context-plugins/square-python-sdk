from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.subscription_action_type import SubscriptionActionTypeOrStr
from .phase import Phase, PhaseDict


class SubscriptionAction(SdkBaseModel):
    """Represents an action as a pending change to a subscription."""

    id: Optional[str] = UNSET
    """The ID of an action scoped to a subscription."""

    type_: Optional[SubscriptionActionTypeOrStr] = Field(default=UNSET, alias="type")
    """Supported types of an action as a pending change to a subscription."""

    effective_date: OptionalNullable[str] = UNSET
    """The ``YYYY-MM-DD``-formatted date when the action occurs on the subscription."""

    monthly_billing_anchor_date: OptionalNullable[int] = UNSET
    """The new billing anchor day value, for a ``CHANGE_BILLING_ANCHOR_DATE`` action."""

    phases: Optional[list[Phase | None]] = UNSET
    """A list of Phases, to pass phase-specific information used in the swap."""

    new_plan_variation_id: OptionalNullable[str] = UNSET
    """The target subscription plan variation that a subscription switches to, for a ``SWAP_PLAN`` action."""


class SubscriptionActionDict(TypedDict):
    id: NotRequired[str]
    type_: NotRequired[SubscriptionActionTypeOrStr]
    effective_date: NotRequired[str | None]
    monthly_billing_anchor_date: NotRequired[int | None]
    phases: NotRequired[list[Phase | PhaseDict | None]]
    new_plan_variation_id: NotRequired[str | None]
