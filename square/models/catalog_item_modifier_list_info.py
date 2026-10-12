from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .catalog_modifier_override import CatalogModifierOverride, CatalogModifierOverrideDict
from .enums.catalog_modifier_toggle_override_type import CatalogModifierToggleOverrideTypeOrStr


class CatalogItemModifierListInfo(SdkBaseModel):
    """Controls how a modifier list is applied to a specific item. This object allows for item-specific customization of
    modifier list behavior and provides the ability to override global modifier list settings."""

    modifier_list_id: str
    """The ID of the ``CatalogModifierList`` controlled by this ``CatalogModifierListInfo``."""

    modifier_overrides: OptionalNullable[list[CatalogModifierOverride]] = UNSET
    """A set of ``CatalogModifierOverride`` objects that override default modifier settings for this item."""

    min_selected_modifiers: OptionalNullable[int] = UNSET
    """The minimum number of modifiers that must be selected from this modifier list. Values:

    - 0: No selection is required.
    - -1: Default value, the attribute was not set by the client. When ``max_selected_modifiers`` is
    also -1, use the minimum and maximum selection values set on the ``CatalogItemModifierList``.
    - &gt;0: The required minimum modifier selections. This can be larger than the total ``CatalogModifiers`` when
        ``allow_quantities`` is enabled.
    - &lt; -1: Invalid. Treated as no selection required."""

    max_selected_modifiers: OptionalNullable[int] = UNSET
    """The maximum number of modifiers that can be selected. Values:

    - 0: No maximum limit.
    - -1: Default value, the attribute was not set by the client. When ``min_selected_modifiers`` is
    also -1, use the minimum and maximum selection values set on the ``CatalogItemModifierList``.
    - &gt;0: The maximum total modifier selections. This can be larger than the total ``CatalogModifiers`` when
        ``allow_quantities`` is enabled.
    - &lt; -1: Invalid. Treated as no maximum limit."""

    enabled: OptionalNullable[bool] = UNSET
    """If ``true``, enable this ``CatalogModifierList``. The default value is ``true``."""

    ordinal: OptionalNullable[int] = UNSET
    """The position of this ``CatalogItemModifierListInfo`` object within the ``modifier_list_info`` list applied to a
    ``CatalogItem`` instance."""

    allow_quantities: Optional[CatalogModifierToggleOverrideTypeOrStr] = UNSET
    """Item level overrides for bool attributes"""

    is_conversational: Optional[CatalogModifierToggleOverrideTypeOrStr] = UNSET
    """Item level overrides for bool attributes"""

    hidden_from_customer_override: Optional[CatalogModifierToggleOverrideTypeOrStr] = UNSET
    """Item level overrides for bool attributes"""


class CatalogItemModifierListInfoDict(TypedDict):
    modifier_list_id: str
    modifier_overrides: NotRequired[list[CatalogModifierOverrideDict] | None]
    min_selected_modifiers: NotRequired[int | None]
    max_selected_modifiers: NotRequired[int | None]
    enabled: NotRequired[bool | None]
    ordinal: NotRequired[int | None]
    allow_quantities: NotRequired[CatalogModifierToggleOverrideTypeOrStr]
    is_conversational: NotRequired[CatalogModifierToggleOverrideTypeOrStr]
    hidden_from_customer_override: NotRequired[CatalogModifierToggleOverrideTypeOrStr]
