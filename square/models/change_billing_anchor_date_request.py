from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ChangeBillingAnchorDateRequest(SdkBaseModel):
    """Defines input parameters in a request to the `ChangeBillingAnchorDate
    <api-endpoint:Subscriptions-ChangeBillingAnchorDate>`__ endpoint."""

    monthly_billing_anchor_date: OptionalNullable[int] = UNSET
    """The anchor day for the billing cycle."""

    effective_date: OptionalNullable[str] = UNSET
    """The ``YYYY-MM-DD``-formatted date when the scheduled ``BILLING_ANCHOR_CHANGE`` action takes place on the
    subscription.

    When this date is unspecified or falls within the current billing cycle, the billing anchor date is changed
    immediately."""


class ChangeBillingAnchorDateRequestDict(TypedDict):
    monthly_billing_anchor_date: NotRequired[int | None]
    effective_date: NotRequired[str | None]
