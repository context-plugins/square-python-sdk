from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_component_details_application_details import (
    DeviceComponentDetailsApplicationDetails,
    DeviceComponentDetailsApplicationDetailsDict,
)
from .device_component_details_battery_details import (
    DeviceComponentDetailsBatteryDetails,
    DeviceComponentDetailsBatteryDetailsDict,
)
from .device_component_details_card_reader_details import (
    DeviceComponentDetailsCardReaderDetails,
    DeviceComponentDetailsCardReaderDetailsDict,
)
from .device_component_details_ethernet_details import (
    DeviceComponentDetailsEthernetDetails,
    DeviceComponentDetailsEthernetDetailsDict,
)
from .device_component_details_wi_fi_details import (
    DeviceComponentDetailsWiFiDetails,
    DeviceComponentDetailsWiFiDetailsDict,
)
from .enums.component_component_type import ComponentComponentTypeOrStr


class Component(SdkBaseModel):
    """The wrapper object for the component entries of a given component type."""

    type_: ComponentComponentTypeOrStr = Field(alias="type")
    """An enum for ComponentType."""

    application_details: Optional[DeviceComponentDetailsApplicationDetails] = UNSET
    card_reader_details: Optional[DeviceComponentDetailsCardReaderDetails] = UNSET
    battery_details: Optional[DeviceComponentDetailsBatteryDetails] = UNSET
    wifi_details: Optional[DeviceComponentDetailsWiFiDetails] = UNSET
    ethernet_details: Optional[DeviceComponentDetailsEthernetDetails] = UNSET


class ComponentDict(TypedDict):
    type_: ComponentComponentTypeOrStr
    application_details: NotRequired[DeviceComponentDetailsApplicationDetailsDict]
    card_reader_details: NotRequired[DeviceComponentDetailsCardReaderDetailsDict]
    battery_details: NotRequired[DeviceComponentDetailsBatteryDetailsDict]
    wifi_details: NotRequired[DeviceComponentDetailsWiFiDetailsDict]
    ethernet_details: NotRequired[DeviceComponentDetailsEthernetDetailsDict]
