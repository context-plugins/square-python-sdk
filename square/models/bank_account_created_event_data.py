from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .bank_account_created_event_object import BankAccountCreatedEventObject, BankAccountCreatedEventObjectDict


class BankAccountCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"bank_account"``."""

    id: Optional[str] = UNSET
    """ID of the affected bank account."""

    object_: Optional[BankAccountCreatedEventObject] = Field(default=UNSET, alias="object")


class BankAccountCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[BankAccountCreatedEventObjectDict]
