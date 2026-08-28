from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CatalogEcomSeoData(SdkBaseModel):
    """SEO data for for a seller's Square Online store."""

    page_title: OptionalNullable[str] = UNSET
    """The SEO title used for the Square Online store."""

    page_description: OptionalNullable[str] = UNSET
    """The SEO description used for the Square Online store."""

    permalink: OptionalNullable[str] = UNSET
    """The SEO permalink used for the Square Online store."""


class CatalogEcomSeoDataDict(TypedDict):
    page_title: NotRequired[str | None]
    page_description: NotRequired[str | None]
    permalink: NotRequired[str | None]
