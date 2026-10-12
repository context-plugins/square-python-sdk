from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address import Address, AddressDict
from .application_details import ApplicationDetails, ApplicationDetailsDict
from .bank_account_payment_details import BankAccountPaymentDetails, BankAccountPaymentDetailsDict
from .buy_now_pay_later_details import BuyNowPayLaterDetails, BuyNowPayLaterDetailsDict
from .card_payment_details import CardPaymentDetails, CardPaymentDetailsDict
from .cash_payment_details import CashPaymentDetails, CashPaymentDetailsDict
from .device_details import DeviceDetails, DeviceDetailsDict
from .digital_wallet_details import DigitalWalletDetails, DigitalWalletDetailsDict
from .electronic_money_details import ElectronicMoneyDetails, ElectronicMoneyDetailsDict
from .external_payment_details import ExternalPaymentDetails, ExternalPaymentDetailsDict
from .money import Money, MoneyDict
from .offline_payment_details import OfflinePaymentDetails, OfflinePaymentDetailsDict
from .processing_fee import ProcessingFee, ProcessingFeeDict
from .risk_evaluation import RiskEvaluation, RiskEvaluationDict
from .square_account_details import SquareAccountDetails, SquareAccountDetailsDict


class Payment(SdkBaseModel):
    """Represents a payment processed by the Square API."""

    id: Optional[str] = UNSET
    """A unique ID for the payment."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the payment was created, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp of when the payment was last updated, in RFC 3339 format."""

    amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    tip_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    total_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    app_fee_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    approved_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    processing_fee: Optional[list[ProcessingFee]] = UNSET
    """The processing fees and fee adjustments assessed by Square for this payment."""

    refunded_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    status: Optional[str] = UNSET
    """Indicates whether the payment is APPROVED, PENDING, COMPLETED, CANCELED, or FAILED."""

    delay_duration: Optional[str] = UNSET
    """The duration of time after the payment's creation when Square automatically applies the ``delay_action`` to the
    payment. This automatic ``delay_action`` applies only to payments that do not reach a terminal state (COMPLETED,
    CANCELED, or FAILED) before the ``delay_duration`` time period.

    This field is specified as a time duration, in RFC 3339 format.

    Notes: This feature is only supported for card payments.

    Default:

    - Card-present payments: "PT36H" (36 hours) from the creation time.
    - Card-not-present payments: "P7D" (7 days) from the creation time."""

    delay_action: OptionalNullable[str] = UNSET
    """The action to be applied to the payment when the ``delay_duration`` has elapsed.

    Current values include ``CANCEL`` and ``COMPLETE``."""

    delayed_until: Optional[str] = UNSET
    """The read-only timestamp of when the ``delay_action`` is automatically applied, in RFC 3339 format.

    Note that this field is calculated by summing the payment's ``delay_duration`` and ``created_at`` fields. The
    ``created_at`` field is generated by Square and might not exactly match the time on your local machine."""

    source_type: Optional[str] = UNSET
    """The source type for this payment.

    Current values include ``CARD``, ``BANK_ACCOUNT``, ``WALLET``, ``BUY_NOW_PAY_LATER``, ``SQUARE_ACCOUNT``, ``CASH``
    and ``EXTERNAL``. For information about these payment source types, see `Take Payments
    <https://developer.squareup.com/docs/payments-api/take-payments>`__."""

    card_details: Optional[CardPaymentDetails] = UNSET
    """Reflects the current status of a card payment. Contains only non-confidential information."""

    cash_details: Optional[CashPaymentDetails] = UNSET
    """Stores details about a cash payment. Contains only non-confidential information. For more information, see `Take
    Cash Payments <https://developer.squareup.com/docs/payments-api/take-payments/cash-payments>`__."""

    bank_account_details: Optional[BankAccountPaymentDetails] = UNSET
    """Additional details about BANK_ACCOUNT type payments."""

    electronic_money_details: Optional[ElectronicMoneyDetails] = UNSET
    """Details specific to electronic money payments."""

    external_details: Optional[ExternalPaymentDetails] = UNSET
    """Stores details about an external payment. Contains only non-confidential information. For more information, see
    `Take External Payments <https://developer.squareup.com/docs/payments-api/take-payments/external-payments>`__."""

    wallet_details: Optional[DigitalWalletDetails] = UNSET
    """Additional details about ``WALLET`` type payments. Contains only non-confidential information."""

    buy_now_pay_later_details: Optional[BuyNowPayLaterDetails] = UNSET
    """Additional details about a Buy Now Pay Later payment type."""

    square_account_details: Optional[SquareAccountDetails] = UNSET
    """Additional details about Square Account payments."""

    location_id: Optional[str] = UNSET
    """The ID of the location associated with the payment."""

    order_id: Optional[str] = UNSET
    """The ID of the order associated with the payment."""

    reference_id: Optional[str] = UNSET
    """An optional ID that associates the payment with an entity in another system."""

    customer_id: Optional[str] = UNSET
    """The ID of the customer associated with the payment. If the ID is not provided in the ``CreatePayment`` request
    that was used to create the ``Payment``, Square may use information in the request (such as the billing and shipping
    address, email address, and payment source) to identify a matching customer profile in the Customer Directory. If
    found, the profile ID is used. If a profile is not found, the API attempts to create an `instant profile
    <https://developer.squareup.com/docs/customers-api/what-it-does#instant-profiles>`__. If the API cannot create an
    instant profile (either because the seller has disabled it or the seller's region prevents creating it), this field
    remains unset. Note that this process is asynchronous and it may take some time before a customer ID is added to the
    payment."""

    employee_id: Optional[str] = UNSET
    """__Deprecated__: Use ``Payment.team_member_id`` instead.

    An optional ID of the employee associated with taking the payment."""

    team_member_id: OptionalNullable[str] = UNSET
    """An optional ID of the `TeamMember <entity:TeamMember>`__ associated with taking the payment."""

    refund_ids: Optional[list[str]] = UNSET
    """A list of ``refund_id``s identifying refunds for the payment."""

    risk_evaluation: Optional[RiskEvaluation] = UNSET
    """Represents fraud risk information for the associated payment.

    When you take a payment through Square's Payments API (using the ``CreatePayment`` endpoint), Square evaluates it
    and assigns a risk level to the payment. Sellers can use this information to determine the course of action (for
    example, provide the goods/services or refund the payment)."""

    terminal_checkout_id: Optional[str] = UNSET
    """An optional ID for a Terminal checkout that is associated with the payment."""

    buyer_email_address: Optional[str] = UNSET
    """The buyer's email address."""

    billing_address: Optional[Address] = UNSET
    """Represents a postal address in a country. For more information, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""

    shipping_address: Optional[Address] = UNSET
    """Represents a postal address in a country. For more information, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""

    note: Optional[str] = UNSET
    """An optional note to include when creating a payment."""

    statement_description_identifier: Optional[str] = UNSET
    """Additional payment information that gets added to the customer's card statement as part of the statement
    description.

    Note that the ``statement_description_identifier`` might get truncated on the statement description to fit the
    required information including the Square identifier (SQ *) and the name of the seller taking the payment."""

    capabilities: Optional[list[str]] = UNSET
    """Actions that can be performed on this payment:
    - ``EDIT_AMOUNT_UP`` - The payment amount can be edited up.
    - ``EDIT_AMOUNT_DOWN`` - The payment amount can be edited down.
    - ``EDIT_TIP_AMOUNT_UP`` - The tip amount can be edited up.
    - ``EDIT_TIP_AMOUNT_DOWN`` - The tip amount can be edited down.
    - ``EDIT_DELAY_ACTION`` - The delay_action can be edited."""

    receipt_number: Optional[str] = UNSET
    """The payment's receipt number. The field is missing if a payment is canceled."""

    receipt_url: Optional[str] = UNSET
    """The URL for the payment's receipt. The field is only populated for COMPLETED payments."""

    device_details: Optional[DeviceDetails] = UNSET
    """Details about the device that took the payment."""

    application_details: Optional[ApplicationDetails] = UNSET
    """Details about the application that took the payment."""

    is_offline_payment: Optional[bool] = UNSET
    """Whether or not this payment was taken offline."""

    offline_payment_details: Optional[OfflinePaymentDetails] = UNSET
    """Details specific to offline payments."""

    version_token: OptionalNullable[str] = UNSET
    """Used for optimistic concurrency. This opaque token identifies a specific version of the ``Payment`` object."""


class PaymentDict(TypedDict):
    id: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    amount_money: NotRequired[MoneyDict]
    tip_money: NotRequired[MoneyDict]
    total_money: NotRequired[MoneyDict]
    app_fee_money: NotRequired[MoneyDict]
    approved_money: NotRequired[MoneyDict]
    processing_fee: NotRequired[list[ProcessingFeeDict]]
    refunded_money: NotRequired[MoneyDict]
    status: NotRequired[str]
    delay_duration: NotRequired[str]
    delay_action: NotRequired[str | None]
    delayed_until: NotRequired[str]
    source_type: NotRequired[str]
    card_details: NotRequired[CardPaymentDetailsDict]
    cash_details: NotRequired[CashPaymentDetailsDict]
    bank_account_details: NotRequired[BankAccountPaymentDetailsDict]
    electronic_money_details: NotRequired[ElectronicMoneyDetailsDict]
    external_details: NotRequired[ExternalPaymentDetailsDict]
    wallet_details: NotRequired[DigitalWalletDetailsDict]
    buy_now_pay_later_details: NotRequired[BuyNowPayLaterDetailsDict]
    square_account_details: NotRequired[SquareAccountDetailsDict]
    location_id: NotRequired[str]
    order_id: NotRequired[str]
    reference_id: NotRequired[str]
    customer_id: NotRequired[str]
    employee_id: NotRequired[str]
    team_member_id: NotRequired[str | None]
    refund_ids: NotRequired[list[str]]
    risk_evaluation: NotRequired[RiskEvaluationDict]
    terminal_checkout_id: NotRequired[str]
    buyer_email_address: NotRequired[str]
    billing_address: NotRequired[AddressDict]
    shipping_address: NotRequired[AddressDict]
    note: NotRequired[str]
    statement_description_identifier: NotRequired[str]
    capabilities: NotRequired[list[str]]
    receipt_number: NotRequired[str]
    receipt_url: NotRequired[str]
    device_details: NotRequired[DeviceDetailsDict]
    application_details: NotRequired[ApplicationDetailsDict]
    is_offline_payment: NotRequired[bool]
    offline_payment_details: NotRequired[OfflinePaymentDetailsDict]
    version_token: NotRequired[str | None]
