from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .catalog_quick_amount import CatalogQuickAmount, CatalogQuickAmountDict
from .enums.catalog_quick_amounts_settings_option import CatalogQuickAmountsSettingsOptionOrStr


class CatalogQuickAmountsSettings(SdkBaseModel):
    """A parent Catalog Object model represents a set of Quick Amounts and the settings control the amounts."""

    option: CatalogQuickAmountsSettingsOptionOrStr
    """Determines a seller's option on Quick Amounts feature."""

    eligible_for_auto_amounts: OptionalNullable[bool] = UNSET
    """Represents location's eligibility for auto amounts The boolean should be consistent with whether there are AUTO
    amounts in the ``amounts``."""

    amounts: Optional[list[CatalogQuickAmount | None]] = UNSET
    """Represents a set of Quick Amounts at this location."""


class CatalogQuickAmountsSettingsDict(TypedDict):
    option: CatalogQuickAmountsSettingsOptionOrStr
    eligible_for_auto_amounts: NotRequired[bool | None]
    amounts: NotRequired[list[CatalogQuickAmount | CatalogQuickAmountDict | None]]
