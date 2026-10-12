from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_account import BankAccount, BankAccountDict
from .error import Error, ErrorDict


class GetBankAccountByV1IdResponse(SdkBaseModel):
    """Response object returned by GetBankAccountByV1Id."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    bank_account: Optional[BankAccount] = UNSET
    """Represents a bank account. For more information about linking a bank account to a Square account, see `Bank
    Accounts API <https://developer.squareup.com/docs/bank-accounts-api>`__."""


class GetBankAccountByV1IdResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    bank_account: NotRequired[BankAccountDict]
