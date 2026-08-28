from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CatalogQueryItemsForTax(SdkBaseModel):
    """The query filter to return the items containing the specified tax IDs."""

    tax_ids: list[str]
    """A set of ``CatalogTax`` IDs to be used to find associated ``CatalogItem``s."""


class CatalogQueryItemsForTaxDict(TypedDict):
    tax_ids: list[str]
