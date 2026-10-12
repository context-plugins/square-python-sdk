from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer import Customer, CustomerDict
from .customer_deleted_event_event_context import CustomerDeletedEventEventContext, CustomerDeletedEventEventContextDict


class CustomerDeletedEventObject(SdkBaseModel):
    """An object that contains the customer associated with the event."""

    customer: Optional[Customer] = UNSET
    """Represents a Square customer profile in the Customer Directory of a Square seller."""

    event_context: Optional[CustomerDeletedEventEventContext] = UNSET
    """Information about the change that triggered the event."""


class CustomerDeletedEventObjectDict(TypedDict):
    customer: NotRequired[CustomerDict]
    event_context: NotRequired[CustomerDeletedEventEventContextDict]
