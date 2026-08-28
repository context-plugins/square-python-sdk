from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.bank_account_status import BankAccountStatusOrStr
from .enums.bank_account_type import BankAccountTypeOrStr
from .enums.country import CountryOrStr
from .enums.currency import CurrencyOrStr


class BankAccount(SdkBaseModel):
    """Represents a bank account. For more information about linking a bank account to a Square account, see `Bank
    Accounts API <https://developer.squareup.com/docs/bank-accounts-api>`__."""

    id: str
    """The unique, Square-issued identifier for the bank account."""

    account_number_suffix: str
    """The last few digits of the account number."""

    country: CountryOrStr
    """Indicates the country associated with another entity, such as a business. Values are in `ISO 3166-1-alpha-2
    format <http://www.iso.org/iso/home/standards/country_codes.htm>`__."""

    currency: CurrencyOrStr
    """Indicates the associated currency for an amount of money. Values correspond to `ISO 4217
    <https://wikipedia.org/wiki/ISO_4217>`__."""

    account_type: BankAccountTypeOrStr
    """Indicates the financial purpose of the bank account."""

    holder_name: str
    """Name of the account holder. This name must match the name on the targeted bank account record."""

    primary_bank_identification_number: str
    """Primary identifier for the bank. For more information, see `Bank Accounts API
    <https://developer.squareup.com/docs/bank-accounts-api>`__."""

    secondary_bank_identification_number: OptionalNullable[str] = UNSET
    """Secondary identifier for the bank. For more information, see `Bank Accounts API
    <https://developer.squareup.com/docs/bank-accounts-api>`__."""

    debit_mandate_reference_id: OptionalNullable[str] = UNSET
    """Reference identifier that will be displayed to UK bank account owners when collecting direct debit authorization.
    Only required for UK bank accounts."""

    reference_id: OptionalNullable[str] = UNSET
    """Client-provided identifier for linking the banking account to an entity in a third-party system (for example, a
    bank account number or a user identifier)."""

    location_id: OptionalNullable[str] = UNSET
    """The location to which the bank account belongs."""

    status: BankAccountStatusOrStr
    """Indicates the current verification status of a ``BankAccount`` object."""

    creditable: bool
    """Indicates whether it is possible for Square to send money to this bank account."""

    debitable: bool
    """Indicates whether it is possible for Square to take money from this bank account."""

    fingerprint: OptionalNullable[str] = UNSET
    """A Square-assigned, unique identifier for the bank account based on the account information. The account
    fingerprint can be used to compare account entries and determine if the they represent the same real-world bank
    account."""

    version: Optional[int] = UNSET
    """The current version of the ``BankAccount``."""

    bank_name: OptionalNullable[str] = UNSET
    """Read only. Name of actual financial institution. For example "Bank of America"."""

    customer_id: Optional[str] = UNSET
    """The ID of the customer who owns the bank account"""


class BankAccountDict(TypedDict):
    id: str
    account_number_suffix: str
    country: CountryOrStr
    currency: CurrencyOrStr
    account_type: BankAccountTypeOrStr
    holder_name: str
    primary_bank_identification_number: str
    secondary_bank_identification_number: NotRequired[str | None]
    debit_mandate_reference_id: NotRequired[str | None]
    reference_id: NotRequired[str | None]
    location_id: NotRequired[str | None]
    status: BankAccountStatusOrStr
    creditable: bool
    debitable: bool
    fingerprint: NotRequired[str | None]
    version: NotRequired[int]
    bank_name: NotRequired[str | None]
    customer_id: NotRequired[str]
