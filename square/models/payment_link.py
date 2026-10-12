from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .checkout_options import CheckoutOptions, CheckoutOptionsDict
from .pre_populated_data import PrePopulatedData, PrePopulatedDataDict


class PaymentLink(SdkBaseModel):
    id: Optional[str] = UNSET
    """The Square-assigned ID of the payment link."""

    version: int
    """The Square-assigned version number, which is incremented each time an update is committed to the payment link."""

    description: OptionalNullable[str] = UNSET
    """The optional description of the ``payment_link`` object. It is primarily for use by your application and is not
    used anywhere."""

    order_id: Optional[str] = UNSET
    """The ID of the order associated with the payment link."""

    checkout_options: Optional[CheckoutOptions] = UNSET
    pre_populated_data: Optional[PrePopulatedData] = UNSET
    """Describes buyer data to prepopulate in the payment form. For more information, see `Optional Checkout
    Configurations <https://developer.squareup.com/docs/checkout-api/optional-checkout-configurations>`__."""

    url: Optional[str] = UNSET
    """The shortened URL of the payment link."""

    long_url: Optional[str] = UNSET
    """The long URL of the payment link."""

    created_at: Optional[str] = UNSET
    """The timestamp when the payment link was created, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp when the payment link was last updated, in RFC 3339 format."""

    payment_note: OptionalNullable[str] = UNSET
    """An optional note. After Square processes the payment, this note is added to the resulting ``Payment``."""


class PaymentLinkDict(TypedDict):
    id: NotRequired[str]
    version: int
    description: NotRequired[str | None]
    order_id: NotRequired[str]
    checkout_options: NotRequired[CheckoutOptionsDict]
    pre_populated_data: NotRequired[PrePopulatedDataDict]
    url: NotRequired[str]
    long_url: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    payment_note: NotRequired[str | None]
