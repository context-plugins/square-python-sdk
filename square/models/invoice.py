from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.invoice_delivery_method import InvoiceDeliveryMethodOrStr
from .enums.invoice_status import InvoiceStatusOrStr
from .invoice_accepted_payment_methods import InvoiceAcceptedPaymentMethods, InvoiceAcceptedPaymentMethodsDict
from .invoice_attachment import InvoiceAttachment, InvoiceAttachmentDict
from .invoice_custom_field import InvoiceCustomField, InvoiceCustomFieldDict
from .invoice_payment_request import InvoicePaymentRequest, InvoicePaymentRequestDict
from .invoice_recipient import InvoiceRecipient, InvoiceRecipientDict
from .money import Money, MoneyDict


class Invoice(SdkBaseModel):
    """Stores information about an invoice. You use the Invoices API to create and manage invoices. For more
    information, see `Invoices API Overview <https://developer.squareup.com/docs/invoices-api/overview>`__."""

    id: Optional[str] = UNSET
    """The Square-assigned ID of the invoice."""

    version: Optional[int] = UNSET
    """The Square-assigned version number, which is incremented each time an update is committed to the invoice."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the location that this invoice is associated with.

    If specified in a ``CreateInvoice`` request, the value must match the ``location_id`` of the associated order."""

    order_id: OptionalNullable[str] = UNSET
    """The ID of the `order <entity:Order>`__ for which the invoice is created. This field is required when creating an
    invoice, and the order must be in the ``OPEN`` state.

    To view the line items and other information for the associated order, call the `RetrieveOrder
    <api-endpoint:Orders-RetrieveOrder>`__ endpoint using the order ID."""

    primary_recipient: Optional[InvoiceRecipient] = UNSET
    """Represents a snapshot of customer data. This object stores customer data that is displayed on the invoice and
    that Square uses to deliver the invoice.

    When you provide a customer ID for a draft invoice, Square retrieves the associated customer profile and populates
    the remaining ``InvoiceRecipient`` fields. You cannot update these fields after the invoice is published. Square
    updates the customer ID in response to a merge operation, but does not update other fields."""

    payment_requests: Optional[list[InvoicePaymentRequest | None]] = UNSET
    """The payment schedule for the invoice, represented by one or more payment requests that define payment settings,
    such as amount due and due date. An invoice supports the following payment request combinations:
    - One balance
    - One deposit with one balance
    - 2–12 installments
    - One deposit with 2–12 installments

    This field is required when creating an invoice. It must contain at least one payment request. All payment requests
    for the invoice must equal the total order amount. For more information, see `Configuring payment requests
    <https://developer.squareup.com/docs/invoices-api/create-publish-invoices#payment-requests>`__.

    Adding ``INSTALLMENT`` payment requests to an invoice requires an `Invoices Plus subscription
    <https://developer.squareup.com/docs/invoices-api/overview#invoices-plus-subscription>`__."""

    delivery_method: Optional[InvoiceDeliveryMethodOrStr] = UNSET
    """Indicates how Square delivers the `invoice <entity:Invoice>`__ to the customer."""

    invoice_number: OptionalNullable[str] = UNSET
    """A user-friendly invoice number that is displayed on the invoice. The value is unique within a location. If not
    provided when creating an invoice, Square assigns a value. It increments from 1 and is padded with zeros making it 7
    characters long (for example, 0000001 and 0000002)."""

    title: OptionalNullable[str] = UNSET
    """The title of the invoice, which is displayed on the invoice."""

    description: OptionalNullable[str] = UNSET
    """The description of the invoice, which is displayed on the invoice."""

    scheduled_at: OptionalNullable[str] = UNSET
    """The timestamp when the invoice is scheduled for processing, in RFC 3339 format. After the invoice is published,
    Square processes the invoice on the specified date, according to the delivery method and payment request settings.

    If the field is not set, Square processes the invoice immediately after it is published."""

    public_url: Optional[str] = UNSET
    """A temporary link to the Square-hosted payment page where the customer can pay the invoice. If the link expires,
    customers can provide the email address or phone number associated with the invoice and request a new link directly
    from the expired payment page.

    This field is added after the invoice is published and reaches the scheduled date (if one is defined)."""

    next_payment_amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    status: Optional[InvoiceStatusOrStr] = UNSET
    """Indicates the status of an `invoice <entity:Invoice>`__."""

    timezone: Optional[str] = UNSET
    r"""The time zone used to interpret calendar dates on the invoice, such as ``due_date``. When an invoice is created,
    this field is set to the ``timezone`` specified for the seller location. The value cannot be changed.

    For example, a payment ``due_date`` of 2021-03-09 with a ``timezone`` of America/Los\_Angeles becomes overdue at
    midnight on March 9 in America/Los\_Angeles (which equals a UTC timestamp of 2021-03-10T08:00:00Z)."""

    created_at: Optional[str] = UNSET
    """The timestamp when the invoice was created, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp when the invoice was last updated, in RFC 3339 format."""

    accepted_payment_methods: Optional[InvoiceAcceptedPaymentMethods] = UNSET
    """The payment methods that customers can use to pay an `invoice <entity:Invoice>`__ on the Square-hosted invoice
    payment page."""

    custom_fields: Optional[list[InvoiceCustomField | None]] = UNSET
    """Additional seller-defined fields that are displayed on the invoice. For more information, see `Custom fields
    <https://developer.squareup.com/docs/invoices-api/overview#custom-fields>`__.

    Adding custom fields to an invoice requires an `Invoices Plus subscription
    <https://developer.squareup.com/docs/invoices-api/overview#invoices-plus-subscription>`__.

    Max: 2 custom fields"""

    subscription_id: Optional[str] = UNSET
    """The ID of the `subscription <entity:Subscription>`__ associated with the invoice. This field is present only on
    subscription billing invoices."""

    sale_or_service_date: OptionalNullable[str] = UNSET
    """The date of the sale or the date that the service is rendered, in ``YYYY-MM-DD`` format. This field can be used
    to specify a past or future date which is displayed on the invoice."""

    payment_conditions: OptionalNullable[str] = UNSET
    """**France only.** The payment terms and conditions that are displayed on the invoice. For more information, see
    `Payment conditions <https://developer.squareup.com/docs/invoices-api/overview#payment-conditions>`__.

    For countries other than France, Square returns an ``INVALID_REQUEST_ERROR`` with a ``BAD_REQUEST`` code and
    "Payment conditions are not supported for this location's country" detail if this field is included in
    ``CreateInvoice`` or ``UpdateInvoice`` requests."""

    store_payment_method_enabled: OptionalNullable[bool] = UNSET
    """Indicates whether to allow a customer to save a credit or debit card as a card on file or a bank transfer as a
    bank account on file. If ``true``, Square displays a __Save my card on file__ or __Save my bank on file__ checkbox
    on the invoice payment page. Stored payment information can be used for future automatic payments. The default value
    is ``false``."""

    attachments: Optional[list[InvoiceAttachment]] = UNSET
    """Metadata about the attachments on the invoice. Invoice attachments are managed using the `CreateInvoiceAttachment
    <api-endpoint:Invoices-CreateInvoiceAttachment>`__ and `DeleteInvoiceAttachment
    <api-endpoint:Invoices-DeleteInvoiceAttachment>`__ endpoints."""

    creator_team_member_id: Optional[str] = UNSET
    """The ID of the `team member <entity:TeamMember>`__ who created the invoice. This field is present only on invoices
    created in the Square Dashboard or Square Invoices app by a logged-in team member."""


class InvoiceDict(TypedDict):
    id: NotRequired[str]
    version: NotRequired[int]
    location_id: NotRequired[str | None]
    order_id: NotRequired[str | None]
    primary_recipient: NotRequired[InvoiceRecipient | InvoiceRecipientDict]
    payment_requests: NotRequired[list[InvoicePaymentRequest | InvoicePaymentRequestDict | None]]
    delivery_method: NotRequired[InvoiceDeliveryMethodOrStr]
    invoice_number: NotRequired[str | None]
    title: NotRequired[str | None]
    description: NotRequired[str | None]
    scheduled_at: NotRequired[str | None]
    public_url: NotRequired[str]
    next_payment_amount_money: NotRequired[Money | MoneyDict]
    status: NotRequired[InvoiceStatusOrStr]
    timezone: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    accepted_payment_methods: NotRequired[InvoiceAcceptedPaymentMethods | InvoiceAcceptedPaymentMethodsDict]
    custom_fields: NotRequired[list[InvoiceCustomField | InvoiceCustomFieldDict | None]]
    subscription_id: NotRequired[str]
    sale_or_service_date: NotRequired[str | None]
    payment_conditions: NotRequired[str | None]
    store_payment_method_enabled: NotRequired[bool | None]
    attachments: NotRequired[list[InvoiceAttachment | InvoiceAttachmentDict]]
    creator_team_member_id: NotRequired[str]
