from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer import Customer, CustomerDict


class CustomerUpdatedEventObject(SdkBaseModel):
    """An object that contains the customer associated with the event."""

    customer: Optional[Customer] = UNSET
    """Represents a Square customer profile in the Customer Directory of a Square seller."""


class CustomerUpdatedEventObjectDict(TypedDict):
    customer: NotRequired[CustomerDict]
