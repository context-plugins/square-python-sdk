from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.invoice_custom_field_placement import InvoiceCustomFieldPlacementOrStr


class InvoiceCustomField(SdkBaseModel):
    """An additional seller-defined and customer-facing field to include on the invoice. For more information, see
    `Custom fields <https://developer.squareup.com/docs/invoices-api/overview#custom-fields>`__.

    Adding custom fields to an invoice requires an `Invoices Plus subscription
    <https://developer.squareup.com/docs/invoices-api/overview#invoices-plus-subscription>`__."""

    label: OptionalNullable[str] = UNSET
    """The label or title of the custom field. This field is required for a custom field."""

    value: OptionalNullable[str] = UNSET
    """The text of the custom field. If omitted, only the label is rendered."""

    placement: Optional[InvoiceCustomFieldPlacementOrStr] = UNSET
    """Indicates where to render a custom field on the Square-hosted invoice page and in emailed or PDF copies of the
    invoice."""


class InvoiceCustomFieldDict(TypedDict):
    label: NotRequired[str | None]
    value: NotRequired[str | None]
    placement: NotRequired[InvoiceCustomFieldPlacementOrStr]
