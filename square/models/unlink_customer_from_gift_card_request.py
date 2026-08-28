from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UnlinkCustomerFromGiftCardRequest(SdkBaseModel):
    """A request to unlink a customer from a gift card."""

    customer_id: str
    """The ID of the customer to unlink from the gift card."""


class UnlinkCustomerFromGiftCardRequestDict(TypedDict):
    customer_id: str
