from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .bank_account_verified_event_object import BankAccountVerifiedEventObject, BankAccountVerifiedEventObjectDict


class BankAccountVerifiedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"bank_account"``."""

    id: Optional[str] = UNSET
    """ID of the affected bank account."""

    object_: Optional[BankAccountVerifiedEventObject] = Field(default=UNSET, alias="object")


class BankAccountVerifiedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[BankAccountVerifiedEventObject | BankAccountVerifiedEventObjectDict]
