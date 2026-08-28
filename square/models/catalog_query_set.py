from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CatalogQuerySet(SdkBaseModel):
    """The query filter to return the search result(s) by exact match of the specified ``attribute_name`` and any of the
    ``attribute_values``."""

    attribute_name: str
    """The name of the attribute to be searched. Matching of the attribute name is exact."""

    attribute_values: list[str]
    """The desired values of the search attribute. Matching of the attribute values is exact and case insensitive. A
    maximum of 250 values may be searched in a request."""


class CatalogQuerySetDict(TypedDict):
    attribute_name: str
    attribute_values: list[str]
