from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class DeviceComponentDetailsMeasurement(SdkBaseModel):
    """A value qualified by unit of measure."""

    value: OptionalNullable[int] = UNSET
    """Value of measure."""


class DeviceComponentDetailsMeasurementDict(TypedDict):
    value: NotRequired[int | None]
