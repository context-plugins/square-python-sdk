from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoiceRequestType(str, Enum):
    """Indicates the type of the payment request. For more information, see `Configuring payment requests
    <https://developer.squareup.com/docs/invoices-api/create-publish-invoices#payment-requests>`__."""

    BALANCE = "BALANCE"
    """A request for a balance payment. The balance amount is computed as follows:

    - If the invoice specifies only a balance payment request, the balance amount is the
    total amount of the associated order.
    - If the invoice also specifies a deposit request, the balance amount is the amount
    remaining after the deposit.

    ``INSTALLMENT`` and ``BALANCE`` payment requests are not allowed in the same invoice."""

    DEPOSIT = "DEPOSIT"
    """A request for a deposit payment. You have the option of specifying an exact amount or a percentage of the total
    order amount. If you request a deposit, it must be due before any other payment requests."""

    INSTALLMENT = "INSTALLMENT"
    """A request for an installment payment. Installments allow buyers to pay the invoice over time. Installments can
    optionally be combined with a deposit.

    Adding ``INSTALLMENT`` payment requests to an invoice requires an `Invoices Plus subscription
    <https://developer.squareup.com/docs/invoices-api/overview#invoices-plus-subscription>`__."""

    __str__ = str.__str__


InvoiceRequestTypeOrStr: TypeAlias = Annotated[InvoiceRequestType | str, open_enum_validator(InvoiceRequestType)]
