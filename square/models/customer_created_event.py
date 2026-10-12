from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .customer_created_event_data import CustomerCreatedEventData, CustomerCreatedEventDataDict


class CustomerCreatedEvent(SdkBaseModel):
    """Published when a `customer <entity:Customer>`__ is created. Subscribe to this event to track customer profiles
    affected by a merge operation. For more information, see `Use Customer Webhooks
    <https://developer.squareup.com/docs/customers-api/use-the-api/customer-webhooks>`__.

    The ``customer`` object in the event notification does not include the ``segment_ids`` field."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the seller associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event. For this object, the value is ``customer.created``."""

    event_id: OptionalNullable[str] = UNSET
    """The unique ID of the event, which is used for `idempotency support
    <https://developer.squareup.com/docs/webhooks/step4manage#webhooks-best-practices>`__."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[CustomerCreatedEventData] = UNSET
    """The data associated with the event."""


class CustomerCreatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[CustomerCreatedEventDataDict]
