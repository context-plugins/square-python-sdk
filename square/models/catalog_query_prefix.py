from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CatalogQueryPrefix(SdkBaseModel):
    """The query filter to return the search result whose named attribute values are prefixed by the specified attribute
    value."""

    attribute_name: str
    """The name of the attribute to be searched."""

    attribute_prefix: str
    """The desired prefix of the search attribute value."""


class CatalogQueryPrefixDict(TypedDict):
    attribute_name: str
    attribute_prefix: str
