from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer import Customer, CustomerDict
from .customer_created_event_event_context import CustomerCreatedEventEventContext, CustomerCreatedEventEventContextDict


class CustomerCreatedEventObject(SdkBaseModel):
    """An object that contains the customer associated with the event."""

    customer: Optional[Customer] = UNSET
    """Represents a Square customer profile in the Customer Directory of a Square seller."""

    event_context: Optional[CustomerCreatedEventEventContext] = UNSET
    """Information about the change that triggered the event."""


class CustomerCreatedEventObjectDict(TypedDict):
    customer: NotRequired[Customer | CustomerDict]
    event_context: NotRequired[CustomerCreatedEventEventContext | CustomerCreatedEventEventContextDict]
