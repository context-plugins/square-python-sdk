from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .catalog_ecom_seo_data import CatalogEcomSeoData, CatalogEcomSeoDataDict
from .catalog_object_category import CatalogObjectCategory, CatalogObjectCategoryDict
from .category_path_to_root_node import CategoryPathToRootNode, CategoryPathToRootNodeDict
from .enums.catalog_category_type import CatalogCategoryTypeOrStr


class CatalogCategory(SdkBaseModel):
    """A category to which a ``CatalogItem`` instance belongs."""

    name: OptionalNullable[str] = UNSET
    """The category name. This is a searchable attribute for use in applicable query filters, and its value length is of
    Unicode code points."""

    image_ids: Optional[list[str | None]] = UNSET
    """The IDs of images associated with this ``CatalogCategory`` instance. Currently these images are not displayed by
    Square, but are free to be displayed in 3rd party applications."""

    category_type: Optional[CatalogCategoryTypeOrStr] = UNSET
    """Indicates the type of a category."""

    parent_category: Optional[CatalogObjectCategory] = UNSET
    """A category that can be assigned to an item or a parent category that can be assigned to another category. For
    example, a clothing category can be assigned to a t-shirt item or be made as the parent category to the pants
    category."""

    is_top_level: OptionalNullable[bool] = UNSET
    """Indicates whether a category is a top level category, which does not have any parent_category."""

    channels: Optional[list[str | None]] = UNSET
    """A list of IDs representing channels, such as a Square Online site, where the category can be made visible."""

    availability_period_ids: Optional[list[str | None]] = UNSET
    """The IDs of the ``CatalogAvailabilityPeriod`` objects associated with the category."""

    online_visibility: OptionalNullable[bool] = UNSET
    """Indicates whether the category is visible (``true``) or hidden (``false``) on all of the seller's Square Online
    sites."""

    root_category: Optional[str] = UNSET
    """The top-level category in a category hierarchy."""

    ecom_seo_data: Optional[CatalogEcomSeoData] = UNSET
    """SEO data for for a seller's Square Online store."""

    path_to_root: Optional[list[CategoryPathToRootNode | None]] = UNSET
    """The path from the category to its root category. The first node of the path is the parent of the category and the
    last is the root category. The path is empty if the category is a root category."""


class CatalogCategoryDict(TypedDict):
    name: NotRequired[str | None]
    image_ids: NotRequired[list[str | None]]
    category_type: NotRequired[CatalogCategoryTypeOrStr]
    parent_category: NotRequired[CatalogObjectCategory | CatalogObjectCategoryDict]
    is_top_level: NotRequired[bool | None]
    channels: NotRequired[list[str | None]]
    availability_period_ids: NotRequired[list[str | None]]
    online_visibility: NotRequired[bool | None]
    root_category: NotRequired[str]
    ecom_seo_data: NotRequired[CatalogEcomSeoData | CatalogEcomSeoDataDict]
    path_to_root: NotRequired[list[CategoryPathToRootNode | CategoryPathToRootNodeDict | None]]
