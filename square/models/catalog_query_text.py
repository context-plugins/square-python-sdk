from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CatalogQueryText(SdkBaseModel):
    """The query filter to return the search result whose searchable attribute values contain all of the specified
    keywords or tokens, independent of the token order or case."""

    keywords: list[str]
    """A list of 1, 2, or 3 search keywords. Keywords with fewer than 3 alphanumeric characters are ignored."""


class CatalogQueryTextDict(TypedDict):
    keywords: list[str]
