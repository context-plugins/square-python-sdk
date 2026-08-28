from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .achdetails import Achdetails, AchdetailsDict
from .error import Error, ErrorDict


class BankAccountPaymentDetails(SdkBaseModel):
    """Additional details about BANK_ACCOUNT type payments."""

    bank_name: OptionalNullable[str] = UNSET
    """The name of the bank associated with the bank account."""

    transfer_type: OptionalNullable[str] = UNSET
    """The type of the bank transfer. The type can be ``ACH`` or ``UNKNOWN``."""

    account_ownership_type: OptionalNullable[str] = UNSET
    """The ownership type of the bank account performing the transfer. The type can be ``INDIVIDUAL``, ``COMPANY``, or
    ``ACCOUNT_TYPE_UNKNOWN``."""

    fingerprint: OptionalNullable[str] = UNSET
    """Uniquely identifies the bank account for this seller and can be used to determine if payments are from the same
    bank account."""

    country: OptionalNullable[str] = UNSET
    """The two-letter ISO code representing the country the bank account is located in."""

    statement_description: OptionalNullable[str] = UNSET
    """The statement description as sent to the bank."""

    ach_details: Optional[Achdetails] = UNSET
    """ACH-specific details about ``BANK_ACCOUNT`` type payments with the ``transfer_type`` of ``ACH``."""

    errors: Optional[list[Error | None]] = UNSET
    """Information about errors encountered during the request."""


class BankAccountPaymentDetailsDict(TypedDict):
    bank_name: NotRequired[str | None]
    transfer_type: NotRequired[str | None]
    account_ownership_type: NotRequired[str | None]
    fingerprint: NotRequired[str | None]
    country: NotRequired[str | None]
    statement_description: NotRequired[str | None]
    ach_details: NotRequired[Achdetails | AchdetailsDict]
    errors: NotRequired[list[Error | ErrorDict | None]]
