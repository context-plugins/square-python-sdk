from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .location_settings_updated_event_object import (
    LocationSettingsUpdatedEventObject,
    LocationSettingsUpdatedEventObjectDict,
)


class LocationSettingsUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the updated object’s type, ``"online_checkout.location_settings"``."""

    id: Optional[str] = UNSET
    """ID of the updated location settings."""

    object_: Optional[LocationSettingsUpdatedEventObject] = Field(default=UNSET, alias="object")


class LocationSettingsUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[LocationSettingsUpdatedEventObject | LocationSettingsUpdatedEventObjectDict]
