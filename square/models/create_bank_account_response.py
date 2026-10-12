from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_account import BankAccount, BankAccountDict
from .error import Error, ErrorDict


class CreateBankAccountResponse(SdkBaseModel):
    """Response object returned by CreateBankAccount."""

    bank_account: Optional[BankAccount] = UNSET
    """Represents a bank account. For more information about linking a bank account to a Square account, see `Bank
    Accounts API <https://developer.squareup.com/docs/bank-accounts-api>`__."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""


class CreateBankAccountResponseDict(TypedDict):
    bank_account: NotRequired[BankAccountDict]
    errors: NotRequired[list[ErrorDict]]
