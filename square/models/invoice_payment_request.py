from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.invoice_automatic_payment_source import InvoiceAutomaticPaymentSourceOrStr
from .enums.invoice_request_method import InvoiceRequestMethodOrStr
from .enums.invoice_request_type import InvoiceRequestTypeOrStr
from .invoice_payment_reminder import InvoicePaymentReminder, InvoicePaymentReminderDict
from .money import Money, MoneyDict


class InvoicePaymentRequest(SdkBaseModel):
    """Represents a payment request for an `invoice <entity:Invoice>`__. Invoices can specify a maximum of 13 payment
    requests, with up to 12 ``INSTALLMENT`` request types. For more information, see `Configuring payment requests
    <https://developer.squareup.com/docs/invoices-api/create-publish-invoices#payment-requests>`__.

    Adding ``INSTALLMENT`` payment requests to an invoice requires an `Invoices Plus subscription
    <https://developer.squareup.com/docs/invoices-api/overview#invoices-plus-subscription>`__."""

    uid: OptionalNullable[str] = UNSET
    """The Square-generated ID of the payment request in an `invoice <entity:Invoice>`__."""

    request_method: Optional[InvoiceRequestMethodOrStr] = UNSET
    """Specifies the action for Square to take for processing the invoice. For example, email the invoice, charge a
    customer's card on file, or do nothing. DEPRECATED at version 2021-01-21. The corresponding ``request_method`` field
    is replaced by the ``Invoice.delivery_method`` and ``InvoicePaymentRequest.automatic_payment_source`` fields."""

    request_type: Optional[InvoiceRequestTypeOrStr] = UNSET
    """Indicates the type of the payment request. For more information, see `Configuring payment requests
    <https://developer.squareup.com/docs/invoices-api/create-publish-invoices#payment-requests>`__."""

    due_date: OptionalNullable[str] = UNSET
    r"""The due date (in the invoice's time zone) for the payment request, in ``YYYY-MM-DD`` format. This field is
    required to create a payment request. If an ``automatic_payment_source`` is defined for the request, Square charges
    the payment source on this date.

    After this date, the invoice becomes overdue. For example, a payment ``due_date`` of 2021-03-09 with a ``timezone``
    of America/Los\_Angeles becomes overdue at midnight on March 9 in America/Los\_Angeles (which equals a UTC timestamp
    of 2021-03-10T08:00:00Z)."""

    fixed_amount_requested_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    percentage_requested: OptionalNullable[str] = UNSET
    """Specifies the amount for the payment request in percentage:

    - When the payment ``request_type`` is ``DEPOSIT``, it is the percentage of the order's total amount.
    - When the payment ``request_type`` is ``INSTALLMENT``, it is the percentage of the order's total less
    the deposit, if requested. The sum of the ``percentage_requested`` in all installment payment requests must be equal
    to 100.

    You cannot specify this when the payment ``request_type`` is ``BALANCE`` or when the payment request specifies the
    ``fixed_amount_requested_money`` field."""

    tipping_enabled: OptionalNullable[bool] = UNSET
    """If set to true, the Square-hosted invoice page (the ``public_url`` field of the invoice) provides a place for the
    customer to pay a tip.

    This field is allowed only on the final payment request and the payment ``request_type`` must be ``BALANCE`` or
    ``INSTALLMENT``."""

    automatic_payment_source: Optional[InvoiceAutomaticPaymentSourceOrStr] = UNSET
    """Indicates the automatic payment method for an `invoice payment request <entity:InvoicePaymentRequest>`__."""

    card_id: OptionalNullable[str] = UNSET
    """The ID of the credit or debit card on file to charge for the payment request. To get the cards on file for a
    customer, call `ListCards <api-endpoint:Cards-ListCards>`__ and include the ``customer_id`` of the invoice
    recipient."""

    reminders: OptionalNullable[list[InvoicePaymentReminder]] = UNSET
    """A list of one or more reminders to send for the payment request."""

    computed_amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    total_completed_amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    rounding_adjustment_included_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class InvoicePaymentRequestDict(TypedDict):
    uid: NotRequired[str | None]
    request_method: NotRequired[InvoiceRequestMethodOrStr]
    request_type: NotRequired[InvoiceRequestTypeOrStr]
    due_date: NotRequired[str | None]
    fixed_amount_requested_money: NotRequired[MoneyDict]
    percentage_requested: NotRequired[str | None]
    tipping_enabled: NotRequired[bool | None]
    automatic_payment_source: NotRequired[InvoiceAutomaticPaymentSourceOrStr]
    card_id: NotRequired[str | None]
    reminders: NotRequired[list[InvoicePaymentReminderDict] | None]
    computed_amount_money: NotRequired[MoneyDict]
    total_completed_amount_money: NotRequired[MoneyDict]
    rounding_adjustment_included_money: NotRequired[MoneyDict]
