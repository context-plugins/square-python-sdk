from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.catalog_modifier_toggle_override_type import CatalogModifierToggleOverrideTypeOrStr


class CatalogModifierOverride(SdkBaseModel):
    """Options to control how to override the default behavior of the specified modifier."""

    modifier_id: str
    """The ID of the ``CatalogModifier`` whose default behavior is being overridden."""

    on_by_default: OptionalNullable[bool] = UNSET
    """__Deprecated__: Use ``on_by_default_override`` instead."""

    hidden_online_override: Optional[CatalogModifierToggleOverrideTypeOrStr] = UNSET
    """Item level overrides for bool attributes"""

    on_by_default_override: Optional[CatalogModifierToggleOverrideTypeOrStr] = UNSET
    """Item level overrides for bool attributes"""


class CatalogModifierOverrideDict(TypedDict):
    modifier_id: str
    on_by_default: NotRequired[bool | None]
    hidden_online_override: NotRequired[CatalogModifierToggleOverrideTypeOrStr]
    on_by_default_override: NotRequired[CatalogModifierToggleOverrideTypeOrStr]
