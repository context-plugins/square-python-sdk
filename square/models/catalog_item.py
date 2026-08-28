from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .catalog_ecom_seo_data import CatalogEcomSeoData, CatalogEcomSeoDataDict
from .catalog_item_food_and_beverage_details import (
    CatalogItemFoodAndBeverageDetails,
    CatalogItemFoodAndBeverageDetailsDict,
)
from .catalog_item_modifier_list_info import CatalogItemModifierListInfo, CatalogItemModifierListInfoDict
from .catalog_item_option_for_item import CatalogItemOptionForItem, CatalogItemOptionForItemDict
from .catalog_object import CatalogObject, CatalogObjectDict
from .catalog_object_category import CatalogObjectCategory, CatalogObjectCategoryDict
from .enums.catalog_item_product_type import CatalogItemProductTypeOrStr


class CatalogItem(SdkBaseModel):
    """A `CatalogObject <entity:CatalogObject>`__ instance of the ``ITEM`` type, also referred to as an item, in the
    catalog."""

    name: OptionalNullable[str] = UNSET
    """The item's name. This is a searchable attribute for use in applicable query filters, its value must not be empty,
    and the length is of Unicode code points."""

    description: OptionalNullable[str] = UNSET
    """The item's description. This is a searchable attribute for use in applicable query filters, and its value length
    is of Unicode code points.

    Deprecated at 2022-07-20, this field is planned to retire in 6 months. You should migrate to use
    ``description_html`` to set the description of the `CatalogItem <entity:CatalogItem>`__ instance. The
    ``description`` and ``description_html`` field values are kept in sync. If you try to set the both fields, the
    ``description_html`` text value overwrites the ``description`` value. Updates in one field are also reflected in the
    other, except for when you use an early version before Square API 2022-07-20 and ``description_html`` is set to
    blank, setting the ``description`` value to null does not nullify ``description_html``."""

    abbreviation: OptionalNullable[str] = UNSET
    """The text of the item's display label in the Square Point of Sale app. Only up to the first five characters of the
    string are used. This attribute is searchable, and its value length is of Unicode code points."""

    label_color: OptionalNullable[str] = UNSET
    """The color of the item's display label in the Square Point of Sale app. This must be a valid hex color code."""

    is_taxable: OptionalNullable[bool] = UNSET
    """Indicates whether the item is taxable (``true``) or non-taxable (``false``). Default is ``true``."""

    category_id: OptionalNullable[str] = UNSET
    """The ID of the item's category, if any. Deprecated since 2023-12-13. Use ``CatalogItem.categories``, instead."""

    buyer_facing_name: OptionalNullable[str] = UNSET
    """The override to a product name to display to users"""

    tax_ids: Optional[list[str | None]] = UNSET
    """A set of IDs indicating the taxes enabled for this item. When updating an item, any taxes listed here will be
    added to the item. Taxes may also be added to or deleted from an item using ``UpdateItemTaxes``."""

    modifier_list_info: Optional[list[CatalogItemModifierListInfo | None]] = UNSET
    """A set of ``CatalogItemModifierListInfo`` objects representing the modifier lists that apply to this item, along
    with the overrides and min and max limits that are specific to this item. Modifier lists may also be added to or
    deleted from an item using ``UpdateItemModifierLists``."""

    variations: Optional[list[CatalogObject | None]] = UNSET
    """A list of `CatalogItemVariation <entity:CatalogItemVariation>`__ objects for this item. An item must have at
    least one variation."""

    product_type: Optional[CatalogItemProductTypeOrStr] = UNSET
    """The type of a CatalogItem. Connect V2 only allows the creation of ``REGULAR`` or ``APPOINTMENTS_SERVICE``
    items."""

    skip_modifier_screen: OptionalNullable[bool] = UNSET
    """If ``false``, the Square Point of Sale app will present the ``CatalogItem``'s details screen immediately,
    allowing the merchant to choose ``CatalogModifier``s before adding the item to the cart. This is the default
    behavior.

    If ``true``, the Square Point of Sale app will immediately add the item to the cart with the pre-selected modifiers,
    and merchants can edit modifiers by drilling down onto the item's details.

    Third-party clients are encouraged to implement similar behaviors."""

    item_options: Optional[list[CatalogItemOptionForItem | None]] = UNSET
    """List of item options IDs for this item. Used to manage and group item variations in a specified order.

    Maximum: 6 item options."""

    ecom_uri: OptionalNullable[str] = UNSET
    """Deprecated. A URI pointing to a published e-commerce product page for the Item."""

    ecom_image_uris: Optional[list[str | None]] = UNSET
    """Deprecated. A comma-separated list of encoded URIs pointing to a set of published e-commerce images for the
    Item."""

    image_ids: Optional[list[str | None]] = UNSET
    """The IDs of images associated with this ``CatalogItem`` instance. These images will be shown to customers in
    Square Online Store. The first image will show up as the icon for this item in POS."""

    sort_name: OptionalNullable[str] = UNSET
    """A name to sort the item by. If this name is unspecified, namely, the ``sort_name`` field is absent, the regular
    ``name`` field is used for sorting. Its value must not be empty.

    It is currently supported for sellers of the Japanese locale only."""

    categories: Optional[list[CatalogObjectCategory | None]] = UNSET
    """The list of categories to which this item belongs. Each entry includes the category ID and an ordinal value that
    determines the item's relative position within that category."""

    description_html: OptionalNullable[str] = UNSET
    """The item's description as expressed in valid HTML elements. The length of this field value, including those of
    HTML tags, is of Unicode points. With application query filters, the text values of the HTML elements and attributes
    are searchable. Invalid or unsupported HTML elements or attributes are ignored.

    Supported HTML elements include:
    - ``a``: Link. Supports linking to website URLs, email address, and telephone numbers.
    - ``b``, ``strong``: Bold text
    - ``br``: Line break
    - ``code``: Computer code
    - ``div``: Section
    - ``h1-h6``: Headings
    - ``i``, ``em``: Italics
    - ``li``: List element
    - ``ol``: Numbered list
    - ``p``: Paragraph
    - ``ul``: Bullet list
    - ``u``: Underline


    Supported HTML attributes include:
    - ``align``: Alignment of the text content
    - ``href``: Link destination
    - ``rel``: Relationship between link's target and source
    - ``target``: Place to open the linked document"""

    description_plaintext: Optional[str] = UNSET
    """A server-generated plaintext version of the ``description_html`` field, without formatting tags."""

    kitchen_name: OptionalNullable[str] = UNSET
    """(Optional) Name that the restaurant wants to display to their kitchen workers instead of the customer-facing
    name. e.g., customer name might be "Big John's Mega Burger" and the kitchen name is "12oz beef burger"
    """

    channels: Optional[list[str | None]] = UNSET
    """A list of IDs representing channels, such as a Square Online site, where the item can be made visible or
    available. This field is read only and cannot be edited."""

    is_archived: OptionalNullable[bool] = UNSET
    """Indicates whether this item is archived (``true``) or not (``false``)."""

    ecom_seo_data: Optional[CatalogEcomSeoData] = UNSET
    """SEO data for for a seller's Square Online store."""

    food_and_beverage_details: Optional[CatalogItemFoodAndBeverageDetails] = UNSET
    """The food and beverage-specific details of a ``FOOD_AND_BEV`` item."""

    reporting_category: Optional[CatalogObjectCategory] = UNSET
    """A category that can be assigned to an item or a parent category that can be assigned to another category. For
    example, a clothing category can be assigned to a t-shirt item or be made as the parent category to the pants
    category."""

    is_alcoholic: OptionalNullable[bool] = UNSET
    """Indicates whether this item is alcoholic (``true``) or not (``false``)."""


class CatalogItemDict(TypedDict):
    name: NotRequired[str | None]
    description: NotRequired[str | None]
    abbreviation: NotRequired[str | None]
    label_color: NotRequired[str | None]
    is_taxable: NotRequired[bool | None]
    category_id: NotRequired[str | None]
    buyer_facing_name: NotRequired[str | None]
    tax_ids: NotRequired[list[str | None]]
    modifier_list_info: NotRequired[list[CatalogItemModifierListInfo | CatalogItemModifierListInfoDict | None]]
    variations: NotRequired[list[CatalogObject | CatalogObjectDict | None]]
    product_type: NotRequired[CatalogItemProductTypeOrStr]
    skip_modifier_screen: NotRequired[bool | None]
    item_options: NotRequired[list[CatalogItemOptionForItem | CatalogItemOptionForItemDict | None]]
    ecom_uri: NotRequired[str | None]
    ecom_image_uris: NotRequired[list[str | None]]
    image_ids: NotRequired[list[str | None]]
    sort_name: NotRequired[str | None]
    categories: NotRequired[list[CatalogObjectCategory | CatalogObjectCategoryDict | None]]
    description_html: NotRequired[str | None]
    description_plaintext: NotRequired[str]
    kitchen_name: NotRequired[str | None]
    channels: NotRequired[list[str | None]]
    is_archived: NotRequired[bool | None]
    ecom_seo_data: NotRequired[CatalogEcomSeoData | CatalogEcomSeoDataDict]
    food_and_beverage_details: NotRequired[CatalogItemFoodAndBeverageDetails | CatalogItemFoodAndBeverageDetailsDict]
    reporting_category: NotRequired[CatalogObjectCategory | CatalogObjectCategoryDict]
    is_alcoholic: NotRequired[bool | None]
