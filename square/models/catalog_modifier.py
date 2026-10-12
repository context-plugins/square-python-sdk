from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .modifier_location_overrides import ModifierLocationOverrides, ModifierLocationOverridesDict
from .money import Money, MoneyDict


class CatalogModifier(SdkBaseModel):
    """A modifier that can be applied to items at the time of sale. For example, a cheese modifier for a burger, or a
    flavor modifier for a serving of ice cream."""

    name: OptionalNullable[str] = UNSET
    """The modifier name. This is a searchable attribute for use in applicable query filters, and its value length is of
    Unicode code points."""

    price_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    on_by_default: OptionalNullable[bool] = UNSET
    """When ``true``, this modifier is selected by default when displaying the modifier list. This setting can be
    overridden at the item level using ``CatalogModifierListInfo.modifier_overrides``."""

    ordinal: OptionalNullable[int] = UNSET
    """Determines where this ``CatalogModifier`` appears in the ``CatalogModifierList``."""

    modifier_list_id: OptionalNullable[str] = UNSET
    """The ID of the ``CatalogModifierList`` associated with this modifier."""

    location_overrides: OptionalNullable[list[ModifierLocationOverrides]] = UNSET
    """Location-specific price overrides."""

    kitchen_name: OptionalNullable[str] = UNSET
    """(Optional) Name that the restaurant wants to display to their kitchen workers instead of the customer-facing
    name. e.g., customer name might be "Double Baconize" and the kitchen name is "Add 2x bacon"
    """

    image_id: OptionalNullable[str] = UNSET
    """The ID of the image associated with this ``CatalogModifier`` instance. Currently this image is not displayed by
    Square, but is free to be displayed in 3rd party applications."""

    hidden_online: OptionalNullable[bool] = UNSET
    """When ``true``, this modifier is hidden from online ordering channels. This setting can be overridden at the item
    level using ``CatalogModifierListInfo.modifier_overrides``."""


class CatalogModifierDict(TypedDict):
    name: NotRequired[str | None]
    price_money: NotRequired[MoneyDict]
    on_by_default: NotRequired[bool | None]
    ordinal: NotRequired[int | None]
    modifier_list_id: NotRequired[str | None]
    location_overrides: NotRequired[list[ModifierLocationOverridesDict] | None]
    kitchen_name: NotRequired[str | None]
    image_id: NotRequired[str | None]
    hidden_online: NotRequired[bool | None]
