from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_account import BankAccount, BankAccountDict


class BankAccountCreatedEventObject(SdkBaseModel):
    bank_account: Optional[BankAccount] = UNSET
    """Represents a bank account. For more information about linking a bank account to a Square account, see `Bank
    Accounts API <https://developer.squareup.com/docs/bank-accounts-api>`__."""


class BankAccountCreatedEventObjectDict(TypedDict):
    bank_account: NotRequired[BankAccount | BankAccountDict]
