from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Coordinates(SdkBaseModel):
    """Latitude and longitude coordinates."""

    latitude: OptionalNullable[float] = UNSET
    """The latitude of the coordinate expressed in degrees."""

    longitude: OptionalNullable[float] = UNSET
    """The longitude of the coordinate expressed in degrees."""


class CoordinatesDict(TypedDict):
    latitude: NotRequired[float | None]
    longitude: NotRequired[float | None]
