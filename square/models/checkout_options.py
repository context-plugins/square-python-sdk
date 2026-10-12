from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .accepted_payment_methods import AcceptedPaymentMethods, AcceptedPaymentMethodsDict
from .custom_field import CustomField, CustomFieldDict
from .money import Money, MoneyDict
from .shipping_fee import ShippingFee, ShippingFeeDict


class CheckoutOptions(SdkBaseModel):
    allow_tipping: OptionalNullable[bool] = UNSET
    """Indicates whether the payment allows tipping."""

    custom_fields: OptionalNullable[list[CustomField]] = UNSET
    """The custom fields requesting information from the buyer."""

    subscription_plan_id: OptionalNullable[str] = UNSET
    """The ID of the subscription plan for the buyer to pay and subscribe. For more information, see `Subscription Plan
    Checkout <https://developer.squareup.com/docs/checkout-api/subscription-plan-checkout>`__."""

    redirect_url: OptionalNullable[str] = UNSET
    """The confirmation page URL to redirect the buyer to after Square processes the payment."""

    merchant_support_email: OptionalNullable[str] = UNSET
    """The email address that buyers can use to contact the seller."""

    ask_for_shipping_address: OptionalNullable[bool] = UNSET
    """Indicates whether to include the address fields in the payment form."""

    accepted_payment_methods: Optional[AcceptedPaymentMethods] = UNSET
    app_fee_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    shipping_fee: Optional[ShippingFee] = UNSET
    enable_coupon: OptionalNullable[bool] = UNSET
    """Indicates whether to include the ``Add coupon`` section for the buyer to provide a Square marketing coupon in the
    payment form."""

    enable_loyalty: OptionalNullable[bool] = UNSET
    """Indicates whether to include the ``REWARDS`` section for the buyer to opt in to loyalty, redeem rewards in the
    payment form, or both."""


class CheckoutOptionsDict(TypedDict):
    allow_tipping: NotRequired[bool | None]
    custom_fields: NotRequired[list[CustomFieldDict] | None]
    subscription_plan_id: NotRequired[str | None]
    redirect_url: NotRequired[str | None]
    merchant_support_email: NotRequired[str | None]
    ask_for_shipping_address: NotRequired[bool | None]
    accepted_payment_methods: NotRequired[AcceptedPaymentMethodsDict]
    app_fee_money: NotRequired[MoneyDict]
    shipping_fee: NotRequired[ShippingFeeDict]
    enable_coupon: NotRequired[bool | None]
    enable_loyalty: NotRequired[bool | None]
