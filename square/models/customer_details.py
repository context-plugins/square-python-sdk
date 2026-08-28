from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CustomerDetails(SdkBaseModel):
    """Details about the customer making the payment."""

    customer_initiated: OptionalNullable[bool] = UNSET
    """Indicates whether the customer initiated the payment."""

    seller_keyed_in: OptionalNullable[bool] = UNSET
    """Indicates that the seller keyed in payment details on behalf of the customer. This is used to flag a payment as
    Mail Order / Telephone Order (MOTO)."""


class CustomerDetailsDict(TypedDict):
    customer_initiated: NotRequired[bool | None]
    seller_keyed_in: NotRequired[bool | None]
