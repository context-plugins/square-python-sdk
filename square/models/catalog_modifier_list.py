from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .catalog_object import CatalogObject, CatalogObjectDict
from .enums.catalog_modifier_list_modifier_type import CatalogModifierListModifierTypeOrStr
from .enums.catalog_modifier_list_selection_type import CatalogModifierListSelectionTypeOrStr


class CatalogModifierList(SdkBaseModel):
    """A container for a list of modifiers, or a text-based modifier. For text-based modifiers, this represents text
    configuration for an item. (For example, custom text to print on a t-shirt). For non text-based modifiers, this
    represents a list of modifiers that can be applied to items at the time of sale. (For example, a list of condiments
    for a hot dog, or a list of ice cream flavors). Each element of the modifier list is a ``CatalogObject`` instance of
    the ``MODIFIER`` type."""

    name: OptionalNullable[str] = UNSET
    """The name of the ``CatalogModifierList`` instance. This is a searchable attribute for use in applicable query
    filters, and its value length is of Unicode code points."""

    ordinal: OptionalNullable[int] = UNSET
    """The position of this ``CatalogModifierList`` within a list of ``CatalogModifierList`` instances."""

    selection_type: Optional[CatalogModifierListSelectionTypeOrStr] = UNSET
    """Indicates whether a CatalogModifierList supports multiple selections."""

    modifiers: Optional[list[CatalogObject | None]] = UNSET
    """A non-empty list of ``CatalogModifier`` objects to be included in the ``CatalogModifierList``, for non text-based
    modifiers when the ``modifier_type`` attribute is ``LIST``. Each element of this list is a ``CatalogObject``
    instance of the ``MODIFIER`` type, containing the following attributes:
    ```
    {
    "id": "{{catalog_modifier_id}}", "type": "MODIFIER", "modifier_data": {{a CatalogModifier instance>}}
    }
    ```"""

    image_ids: Optional[list[str | None]] = UNSET
    """The IDs of images associated with this ``CatalogModifierList`` instance. Currently these images are not displayed
    on Square products, but may be displayed in 3rd-party applications."""

    allow_quantities: OptionalNullable[bool] = UNSET
    """When ``true``, allows multiple quantities of the same modifier to be selected."""

    is_conversational: OptionalNullable[bool] = UNSET
    """True if modifiers belonging to this list can be used conversationally."""

    modifier_type: Optional[CatalogModifierListModifierTypeOrStr] = UNSET
    """Defines the type of ``CatalogModifierList``."""

    max_length: OptionalNullable[int] = UNSET
    """The maximum length, in Unicode points, of the text string of the text-based modifier as represented by this
    ``CatalogModifierList`` object with the ``modifier_type`` set to ``TEXT``."""

    text_required: OptionalNullable[bool] = UNSET
    """Whether the text string must be a non-empty string (``true``) or not (``false``) for a text-based modifier as
    represented by this ``CatalogModifierList`` object with the ``modifier_type`` set to ``TEXT``."""

    internal_name: OptionalNullable[str] = UNSET
    """A note for internal use by the business.

    For example, for a text-based modifier applied to a T-shirt item, if the buyer-supplied text of "Hello, Kitty!" is
    to be printed on the T-shirt, this ``internal_name`` attribute can be "Use italic face" as an instruction for the
    business to follow.

    For non text-based modifiers, this ``internal_name`` attribute can be used to include SKUs, internal codes, or
    supplemental descriptions for internal use."""

    min_selected_modifiers: OptionalNullable[int] = UNSET
    """The minimum number of modifiers that must be selected from this list. The value can be overridden with
    ``CatalogItemModifierListInfo``.

    Values:

    - 0: No selection is required.
    - -1: Default value, the attribute was not set by the client. Treated as no selection required.
    - &gt;0: The required minimum modifier selections. This can be larger than the total ``CatalogModifiers`` when
        ``allow_quantities`` is enabled.
    - &lt; -1: Invalid. Treated as no selection required."""

    max_selected_modifiers: OptionalNullable[int] = UNSET
    """The maximum number of modifiers that must be selected from this list. The value can be overridden with
    ``CatalogItemModifierListInfo``.

    Values:

    - 0: No maximum limit.
    - -1: Default value, the attribute was not set by the client. Treated as no maximum limit.
    - &gt;0: The maximum total modifier selections. This can be larger than the total ``CatalogModifiers`` when
        ``allow_quantities`` is enabled.
    - &lt; -1: Invalid. Treated as no maximum limit."""

    hidden_from_customer: OptionalNullable[bool] = UNSET
    """If ``true``, modifiers from this list are hidden from customer receipts. The default value is ``false``. This
    setting can be overridden with ``CatalogItemModifierListInfo.hidden_from_customer_override``."""


class CatalogModifierListDict(TypedDict):
    name: NotRequired[str | None]
    ordinal: NotRequired[int | None]
    selection_type: NotRequired[CatalogModifierListSelectionTypeOrStr]
    modifiers: NotRequired[list[CatalogObject | CatalogObjectDict | None]]
    image_ids: NotRequired[list[str | None]]
    allow_quantities: NotRequired[bool | None]
    is_conversational: NotRequired[bool | None]
    modifier_type: NotRequired[CatalogModifierListModifierTypeOrStr]
    max_length: NotRequired[int | None]
    text_required: NotRequired[bool | None]
    internal_name: NotRequired[str | None]
    min_selected_modifiers: NotRequired[int | None]
    max_selected_modifiers: NotRequired[int | None]
    hidden_from_customer: NotRequired[bool | None]
