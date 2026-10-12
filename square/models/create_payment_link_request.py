from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .checkout_options import CheckoutOptions, CheckoutOptionsDict
from .order import Order, OrderDict
from .pre_populated_data import PrePopulatedData, PrePopulatedDataDict
from .quick_pay import QuickPay, QuickPayDict


class CreatePaymentLinkRequest(SdkBaseModel):
    idempotency_key: Optional[str] = UNSET
    """A unique string that identifies this ``CreatePaymentLinkRequest`` request. If you do not provide a unique string
    (or provide an empty string as the value), the endpoint treats each request as independent.

    For more information, see `Idempotency <https://developer.squareup.com/docs/working-with-apis/idempotency>`__."""

    description: Optional[str] = UNSET
    """A description of the payment link. You provide this optional description that is useful in your application
    context. It is not used anywhere."""

    quick_pay: Optional[QuickPay] = UNSET
    """Describes an ad hoc item and price to generate a quick pay checkout link. For more information, see `Quick Pay
    Checkout <https://developer.squareup.com/docs/checkout-api/quick-pay-checkout>`__."""

    order: Optional[Order] = UNSET
    """Contains all information related to a single order to process with Square, including line items that specify the
    products to purchase. ``Order`` objects also include information about any associated tenders, refunds, and returns.

    All Connect V2 Transactions have all been converted to Orders including all associated itemization data."""

    checkout_options: Optional[CheckoutOptions] = UNSET
    pre_populated_data: Optional[PrePopulatedData] = UNSET
    """Describes buyer data to prepopulate in the payment form. For more information, see `Optional Checkout
    Configurations <https://developer.squareup.com/docs/checkout-api/optional-checkout-configurations>`__."""

    payment_note: Optional[str] = UNSET
    """A note for the payment. After processing the payment, Square adds this note to the resulting ``Payment``."""


class CreatePaymentLinkRequestDict(TypedDict):
    idempotency_key: NotRequired[str]
    description: NotRequired[str]
    quick_pay: NotRequired[QuickPayDict]
    order: NotRequired[OrderDict]
    checkout_options: NotRequired[CheckoutOptionsDict]
    pre_populated_data: NotRequired[PrePopulatedDataDict]
    payment_note: NotRequired[str]
