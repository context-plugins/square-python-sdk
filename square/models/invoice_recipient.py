from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address import Address, AddressDict
from .invoice_recipient_tax_ids import InvoiceRecipientTaxIds, InvoiceRecipientTaxIdsDict


class InvoiceRecipient(SdkBaseModel):
    """Represents a snapshot of customer data. This object stores customer data that is displayed on the invoice and
    that Square uses to deliver the invoice.

    When you provide a customer ID for a draft invoice, Square retrieves the associated customer profile and populates
    the remaining ``InvoiceRecipient`` fields. You cannot update these fields after the invoice is published. Square
    updates the customer ID in response to a merge operation, but does not update other fields."""

    customer_id: OptionalNullable[str] = UNSET
    """The ID of the customer. This is the customer profile ID that you provide when creating a draft invoice."""

    given_name: Optional[str] = UNSET
    """The recipient's given (that is, first) name."""

    family_name: Optional[str] = UNSET
    """The recipient's family (that is, last) name."""

    email_address: Optional[str] = UNSET
    """The recipient's email address."""

    address: Optional[Address] = UNSET
    """Represents a postal address in a country. For more information, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""

    phone_number: Optional[str] = UNSET
    """The recipient's phone number."""

    company_name: Optional[str] = UNSET
    """The name of the recipient's company."""

    tax_ids: Optional[InvoiceRecipientTaxIds] = UNSET
    """Represents the tax IDs for an invoice recipient. The country of the seller account determines whether the
    corresponding ``tax_ids`` field is available for the customer. For more information, see `Invoice recipient tax IDs
    <https://developer.squareup.com/docs/invoices-api/overview#recipient-tax-ids>`__."""


class InvoiceRecipientDict(TypedDict):
    customer_id: NotRequired[str | None]
    given_name: NotRequired[str]
    family_name: NotRequired[str]
    email_address: NotRequired[str]
    address: NotRequired[Address | AddressDict]
    phone_number: NotRequired[str]
    company_name: NotRequired[str]
    tax_ids: NotRequired[InvoiceRecipientTaxIds | InvoiceRecipientTaxIdsDict]
