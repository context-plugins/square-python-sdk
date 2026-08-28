from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateBankAccountRequest(SdkBaseModel):
    """Request object for linking a bank account to a Square account"""

    idempotency_key: str
    """Unique ID. For more information, see the `Idempotency
    <https://developer.squareup.com/docs/working-with-apis/idempotency>`__."""

    source_id: str
    """The ID of the source that represents the bank account information to be stored. This field accepts the payment
    token created by WebSDK"""

    customer_id: Optional[str] = UNSET
    """The ID of the customer associated with the bank account to be stored."""


class CreateBankAccountRequestDict(TypedDict):
    idempotency_key: str
    source_id: str
    customer_id: NotRequired[str]
