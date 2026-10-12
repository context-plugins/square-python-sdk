from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .felica_details import FelicaDetails, FelicaDetailsDict


class ElectronicMoneyDetails(SdkBaseModel):
    """Details specific to electronic money payments."""

    felica_details: Optional[FelicaDetails] = UNSET
    """Details for Felica payments."""


class ElectronicMoneyDetailsDict(TypedDict):
    felica_details: NotRequired[FelicaDetailsDict]
