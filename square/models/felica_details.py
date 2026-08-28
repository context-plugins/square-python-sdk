from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.felica_details_felica_brand import FelicaDetailsFelicaBrandOrStr


class FelicaDetails(SdkBaseModel):
    """Details for Felica payments."""

    terminal_id: OptionalNullable[str] = UNSET
    """The terminal id for a Felica payment."""

    felica_masked_card_number: OptionalNullable[str] = UNSET
    """The masked card number for a Felica payment."""

    felica_brand: Optional[FelicaDetailsFelicaBrandOrStr] = UNSET
    """A Felica card's "sub-brand"--the actual brand on the Felica card"""


class FelicaDetailsDict(TypedDict):
    terminal_id: NotRequired[str | None]
    felica_masked_card_number: NotRequired[str | None]
    felica_brand: NotRequired[FelicaDetailsFelicaBrandOrStr]
