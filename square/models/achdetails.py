from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Achdetails(SdkBaseModel):
    """ACH-specific details about ``BANK_ACCOUNT`` type payments with the ``transfer_type`` of ``ACH``."""

    routing_number: OptionalNullable[str] = UNSET
    """The routing number for the bank account."""

    account_number_suffix: OptionalNullable[str] = UNSET
    """The last few digits of the bank account number."""

    account_type: OptionalNullable[str] = UNSET
    """The type of the bank account performing the transfer. The account type can be ``CHECKING``, ``SAVINGS``, or
    ``UNKNOWN``."""


class AchdetailsDict(TypedDict):
    routing_number: NotRequired[str | None]
    account_number_suffix: NotRequired[str | None]
    account_type: NotRequired[str | None]
