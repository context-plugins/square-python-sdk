from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.subscription_status import SubscriptionStatusOrStr
from .money import Money, MoneyDict
from .phase import Phase, PhaseDict
from .subscription_action import SubscriptionAction, SubscriptionActionDict
from .subscription_source import SubscriptionSource, SubscriptionSourceDict


class Subscription(SdkBaseModel):
    """Represents a subscription purchased by a customer.

    For more information, see `Manage Subscriptions
    <https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions>`__."""

    id: Optional[str] = UNSET
    """The Square-assigned ID of the subscription."""

    location_id: Optional[str] = UNSET
    """The ID of the location associated with the subscription."""

    plan_variation_id: Optional[str] = UNSET
    """The ID of the subscribed-to `subscription plan variation <entity:CatalogSubscriptionPlanVariation>`__."""

    customer_id: Optional[str] = UNSET
    """The ID of the subscribing `customer <entity:Customer>`__ profile."""

    start_date: Optional[str] = UNSET
    """The ``YYYY-MM-DD``-formatted date (for example, 2013-01-15) to start the subscription."""

    canceled_date: OptionalNullable[str] = UNSET
    """The ``YYYY-MM-DD``-formatted date (for example, 2013-01-15) to cancel the subscription, when the subscription
    status changes to ``CANCELED`` and the subscription billing stops.

    If this field is not set, the subscription ends according its subscription plan.

    This field cannot be updated, other than being cleared."""

    charged_through_date: Optional[str] = UNSET
    """The ``YYYY-MM-DD``-formatted date up to when the subscriber is invoiced for the subscription.

    After the invoice is sent for a given billing period, this date will be the last day of the billing period. For
    example, suppose for the month of May a subscriber gets an invoice (or charged the card) on May 1. For the monthly
    billing scenario, this date is then set to May 31."""

    status: Optional[SubscriptionStatusOrStr] = UNSET
    """Supported subscription statuses."""

    tax_percentage: OptionalNullable[str] = UNSET
    """The tax amount applied when billing the subscription. The percentage is expressed in decimal form, using a
    ``'.'`` as the decimal separator and without a ``'%'`` sign. For example, a value of ``7.5`` corresponds to 7.5%."""

    invoice_ids: Optional[list[str]] = UNSET
    """The IDs of the `invoices <entity:Invoice>`__ created for the subscription, listed in order when the invoices were
    created (newest invoices appear first)."""

    price_override_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    version: Optional[int] = UNSET
    """The version of the object. When updating an object, the version supplied must match the version in the database,
    otherwise the write will be rejected as conflicting."""

    created_at: Optional[str] = UNSET
    """The timestamp when the subscription was created, in RFC 3339 format."""

    card_id: OptionalNullable[str] = UNSET
    """The ID of the `subscriber's <entity:Customer>`__ `card <entity:Card>`__ used to charge for the subscription."""

    timezone: Optional[str] = UNSET
    """Timezone that will be used in date calculations for the subscription. Defaults to the timezone of the location
    based on ``location_id``. Format: the IANA Timezone Database identifier for the location timezone (for example,
    ``America/Los_Angeles``)."""

    source: Optional[SubscriptionSource] = UNSET
    """The origination details of the subscription."""

    actions: Optional[list[SubscriptionAction | None]] = UNSET
    """The list of scheduled actions on this subscription. It is set only in the response from `RetrieveSubscription
    <api-endpoint:Subscriptions-RetrieveSubscription>`__ with the query parameter of ``include=actions`` or from
    `SearchSubscriptions <api-endpoint:Subscriptions-SearchSubscriptions>`__ with the input parameter of
    ``include:["actions"]``."""

    monthly_billing_anchor_date: Optional[int] = UNSET
    """The day of the month on which the subscription will issue invoices and publish orders."""

    phases: Optional[list[Phase]] = UNSET
    """array of phases for this subscription"""

    completed_date: OptionalNullable[str] = UNSET
    """The ``YYYY-MM-DD``-formatted date when the subscription enters a terminal state."""


class SubscriptionDict(TypedDict):
    id: NotRequired[str]
    location_id: NotRequired[str]
    plan_variation_id: NotRequired[str]
    customer_id: NotRequired[str]
    start_date: NotRequired[str]
    canceled_date: NotRequired[str | None]
    charged_through_date: NotRequired[str]
    status: NotRequired[SubscriptionStatusOrStr]
    tax_percentage: NotRequired[str | None]
    invoice_ids: NotRequired[list[str]]
    price_override_money: NotRequired[Money | MoneyDict]
    version: NotRequired[int]
    created_at: NotRequired[str]
    card_id: NotRequired[str | None]
    timezone: NotRequired[str]
    source: NotRequired[SubscriptionSource | SubscriptionSourceDict]
    actions: NotRequired[list[SubscriptionAction | SubscriptionActionDict | None]]
    monthly_billing_anchor_date: NotRequired[int]
    phases: NotRequired[list[Phase | PhaseDict]]
    completed_date: NotRequired[str | None]
