from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MeasurementUnitCustom(SdkBaseModel):
    """The information needed to define a custom unit, provided by the seller."""

    name: str
    """The name of the custom unit, for example "bushel"."""

    abbreviation: str
    """The abbreviation of the custom unit, such as "bsh" (bushel). This appears in the cart for the Point of Sale app,
    and in reports."""


class MeasurementUnitCustomDict(TypedDict):
    name: str
    abbreviation: str
