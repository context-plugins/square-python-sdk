from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.tender_bank_account_details_status import TenderBankAccountDetailsStatusOrStr


class TenderBankAccountDetails(SdkBaseModel):
    """Represents the details of a tender with ``type`` ``BANK_ACCOUNT``.

    See `BankAccountPaymentDetails <entity:BankAccountPaymentDetails>`__ for more exposed details of a bank account
    payment."""

    status: Optional[TenderBankAccountDetailsStatusOrStr] = UNSET
    """Indicates the bank account payment's current status."""


class TenderBankAccountDetailsDict(TypedDict):
    status: NotRequired[TenderBankAccountDetailsStatusOrStr]
