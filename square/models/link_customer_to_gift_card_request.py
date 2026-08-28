from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LinkCustomerToGiftCardRequest(SdkBaseModel):
    """A request to link a customer to a gift card."""

    customer_id: str
    """The ID of the customer to link to the gift card."""


class LinkCustomerToGiftCardRequestDict(TypedDict):
    customer_id: str
