from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .bank_account_created_event_data import BankAccountCreatedEventData, BankAccountCreatedEventDataDict


class BankAccountCreatedEvent(SdkBaseModel):
    """Published when you link an external bank account to a Square account in the Seller Dashboard. Square sets the
    initial status to ``VERIFICATION_IN_PROGRESS`` and publishes the event."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the target location associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents, ``"bank_account.created"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """Timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[BankAccountCreatedEventData] = UNSET


class BankAccountCreatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    location_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[BankAccountCreatedEventDataDict]
