from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_info_response_limits import CatalogInfoResponseLimits, CatalogInfoResponseLimitsDict
from .error import Error, ErrorDict
from .standard_unit_description_group import StandardUnitDescriptionGroup, StandardUnitDescriptionGroupDict


class CatalogInfoResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    limits: Optional[CatalogInfoResponseLimits] = UNSET
    standard_unit_description_group: Optional[StandardUnitDescriptionGroup] = UNSET
    """Group of standard measurement units."""


class CatalogInfoResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    limits: NotRequired[CatalogInfoResponseLimitsDict]
    standard_unit_description_group: NotRequired[StandardUnitDescriptionGroupDict]
