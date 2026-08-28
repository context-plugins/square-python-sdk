from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict
from .phase import Phase, PhaseDict
from .subscription_source import SubscriptionSource, SubscriptionSourceDict


class CreateSubscriptionRequest(SdkBaseModel):
    """Defines input parameters in a request to the `CreateSubscription
    <api-endpoint:Subscriptions-CreateSubscription>`__ endpoint."""

    idempotency_key: Optional[str] = UNSET
    """A unique string that identifies this ``CreateSubscription`` request. If you do not provide a unique string (or
    provide an empty string as the value), the endpoint treats each request as independent.

    For more information, see `Idempotency keys
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""

    location_id: str
    """The ID of the location the subscription is associated with."""

    plan_variation_id: Optional[str] = UNSET
    """The ID of the `subscription plan variation
    <https://developer.squareup.com/docs/subscriptions-api/plans-and-variations#plan-variations>`__ created using the
    Catalog API."""

    customer_id: str
    """The ID of the `customer <entity:Customer>`__ subscribing to the subscription plan variation."""

    start_date: Optional[str] = UNSET
    """The ``YYYY-MM-DD``-formatted date to start the subscription. If it is unspecified, the subscription starts
    immediately."""

    canceled_date: Optional[str] = UNSET
    """The ``YYYY-MM-DD``-formatted date when the newly created subscription is scheduled for cancellation.

    This date overrides the cancellation date set in the plan variation configuration. If the cancellation date is
    earlier than the end date of a subscription cycle, the subscription stops at the canceled date and the subscriber is
    sent a prorated invoice at the beginning of the canceled cycle.

    When the subscription plan of the newly created subscription has a fixed number of cycles and the ``canceled_date``
    occurs before the subscription plan completes, the specified ``canceled_date`` sets the date when the subscription
    stops through the end of the last cycle."""

    tax_percentage: Optional[str] = UNSET
    """The tax to add when billing the subscription. The percentage is expressed in decimal form, using a ``'.'`` as the
    decimal separator and without a ``'%'`` sign. For example, a value of 7.5 corresponds to 7.5%."""

    price_override_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    card_id: Optional[str] = UNSET
    """The ID of the `subscriber's <entity:Customer>`__ `card <entity:Card>`__ to charge. If it is not specified, the
    subscriber receives an invoice via email with a link to pay for their subscription."""

    timezone: Optional[str] = UNSET
    """The timezone that is used in date calculations for the subscription. If unset, defaults to the location timezone.
    If a timezone is not configured for the location, defaults to "America/New_York". Format: the IANA Timezone Database
    identifier for the location timezone. For a list of time zones, see `List of tz database time zones
    <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__."""

    source: Optional[SubscriptionSource] = UNSET
    """The origination details of the subscription."""

    monthly_billing_anchor_date: Optional[int] = UNSET
    """The day-of-the-month to change the billing date to."""

    phases: Optional[list[Phase]] = UNSET
    """array of phases for this subscription"""


class CreateSubscriptionRequestDict(TypedDict):
    idempotency_key: NotRequired[str]
    location_id: str
    plan_variation_id: NotRequired[str]
    customer_id: str
    start_date: NotRequired[str]
    canceled_date: NotRequired[str]
    tax_percentage: NotRequired[str]
    price_override_money: NotRequired[Money | MoneyDict]
    card_id: NotRequired[str]
    timezone: NotRequired[str]
    source: NotRequired[SubscriptionSource | SubscriptionSourceDict]
    monthly_billing_anchor_date: NotRequired[int]
    phases: NotRequired[list[Phase | PhaseDict]]
