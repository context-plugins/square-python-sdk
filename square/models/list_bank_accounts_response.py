from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bank_account import BankAccount, BankAccountDict
from .error import Error, ErrorDict


class ListBankAccountsResponse(SdkBaseModel):
    """Response object returned by ListBankAccounts."""

    bank_accounts: Optional[list[BankAccount]] = UNSET
    """List of BankAccounts associated with this account."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    cursor: Optional[str] = UNSET
    """When a response is truncated, it includes a cursor that you can use in a subsequent request to fetch next set of
    bank accounts. If empty, this is the final response.

    For more information, see `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__."""


class ListBankAccountsResponseDict(TypedDict):
    bank_accounts: NotRequired[list[BankAccount | BankAccountDict]]
    errors: NotRequired[list[Error | ErrorDict]]
    cursor: NotRequired[str]
