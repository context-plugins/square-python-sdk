from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .standard_unit_description import StandardUnitDescription, StandardUnitDescriptionDict


class StandardUnitDescriptionGroup(SdkBaseModel):
    """Group of standard measurement units."""

    standard_unit_descriptions: Optional[list[StandardUnitDescription | None]] = UNSET
    """List of standard (non-custom) measurement units in this description group."""

    language_code: OptionalNullable[str] = UNSET
    """IETF language tag."""


class StandardUnitDescriptionGroupDict(TypedDict):
    standard_unit_descriptions: NotRequired[list[StandardUnitDescription | StandardUnitDescriptionDict | None]]
    language_code: NotRequired[str | None]
