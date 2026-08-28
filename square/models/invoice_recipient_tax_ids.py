from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvoiceRecipientTaxIds(SdkBaseModel):
    """Represents the tax IDs for an invoice recipient. The country of the seller account determines whether the
    corresponding ``tax_ids`` field is available for the customer. For more information, see `Invoice recipient tax IDs
    <https://developer.squareup.com/docs/invoices-api/overview#recipient-tax-ids>`__."""

    eu_vat: Optional[str] = UNSET
    """The EU VAT identification number for the invoice recipient. For example, ``IE3426675K``."""


class InvoiceRecipientTaxIdsDict(TypedDict):
    eu_vat: NotRequired[str]
