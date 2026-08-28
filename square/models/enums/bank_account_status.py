from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankAccountStatus(str, Enum):
    """Indicates the current verification status of a ``BankAccount`` object."""

    VERIFICATION_IN_PROGRESS = "VERIFICATION_IN_PROGRESS"
    """Indicates that the verification process has started. Some features (for example, creditable or debitable) may be
    provisionally enabled on the bank account."""

    VERIFIED = "VERIFIED"
    """Indicates that the bank account was successfully verified."""

    DISABLED = "DISABLED"
    """Indicates that the bank account is disabled and is permanently unusable for funds transfer. A bank account can be
    disabled because of a failed verification attempt or a failed deposit attempt."""

    __str__ = str.__str__


BankAccountStatusOrStr: TypeAlias = Annotated[BankAccountStatus | str, open_enum_validator(BankAccountStatus)]
