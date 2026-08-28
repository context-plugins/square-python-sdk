from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CancelInvoiceRequest(SdkBaseModel):
    """Describes a ``CancelInvoice`` request."""

    version: int
    """The version of the `invoice <entity:Invoice>`__ to cancel. If you do not know the version, you can call
    `GetInvoice <api-endpoint:Invoices-GetInvoice>`__ or `ListInvoices <api-endpoint:Invoices-ListInvoices>`__."""


class CancelInvoiceRequestDict(TypedDict):
    version: int
