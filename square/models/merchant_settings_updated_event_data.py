from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .merchant_settings_updated_event_object import (
    MerchantSettingsUpdatedEventObject,
    MerchantSettingsUpdatedEventObjectDict,
)


class MerchantSettingsUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the updated object’s type, ``"online_checkout.merchant_settings"``."""

    id: Optional[str] = UNSET
    """ID of the updated merchant settings."""

    object_: Optional[MerchantSettingsUpdatedEventObject] = Field(default=UNSET, alias="object")


class MerchantSettingsUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[MerchantSettingsUpdatedEventObject | MerchantSettingsUpdatedEventObjectDict]
