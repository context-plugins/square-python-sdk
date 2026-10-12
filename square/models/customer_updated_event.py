from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .customer_updated_event_data import CustomerUpdatedEventData, CustomerUpdatedEventDataDict


class CustomerUpdatedEvent(SdkBaseModel):
    """Published when a `customer <entity:Customer>`__ is updated. For more information, see `Use Customer Webhooks
    <https://developer.squareup.com/docs/customers-api/use-the-api/customer-webhooks>`__.

    Updates to the 'segment_ids' customer field does not invoke a ``customer.updated`` event. In addition, the
    ``customer`` object in the event notification does not include this field."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the seller associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event. For this object, the value is ``customer.updated``."""

    event_id: OptionalNullable[str] = UNSET
    """The unique ID of the event, which is used for `idempotency support
    <https://developer.squareup.com/docs/webhooks/step4manage#webhooks-best-practices>`__."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[CustomerUpdatedEventData] = UNSET
    """The data associated with the event."""


class CustomerUpdatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[CustomerUpdatedEventDataDict]
