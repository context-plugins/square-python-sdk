from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_segment import CustomerSegment, CustomerSegmentDict
from .error import Error, ErrorDict


class RetrieveCustomerSegmentResponse(SdkBaseModel):
    """Defines the fields that are included in the response body for requests to the ``RetrieveCustomerSegment``
    endpoint.

    Either ``errors`` or ``segment`` is present in a given response (never both)."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    segment: Optional[CustomerSegment] = UNSET
    """Represents a group of customer profiles that match one or more predefined filter criteria.

    Segments (also known as Smart Groups) are defined and created within the Customer Directory in the Square Seller
    Dashboard or Point of Sale."""


class RetrieveCustomerSegmentResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    segment: NotRequired[CustomerSegment | CustomerSegmentDict]
