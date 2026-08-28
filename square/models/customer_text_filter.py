from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CustomerTextFilter(SdkBaseModel):
    """A filter to select customers based on exact or fuzzy matching of customer attributes against a specified query.
    Depending on the customer attributes, the filter can be case-sensitive. This filter can be exact or fuzzy, but it
    cannot be both."""

    exact: OptionalNullable[str] = UNSET
    """Use the exact filter to select customers whose attributes match exactly the specified query."""

    fuzzy: OptionalNullable[str] = UNSET
    """Use the fuzzy filter to select customers whose attributes match the specified query in a fuzzy manner. When the
    fuzzy option is used, search queries are tokenized, and then each query token must be matched somewhere in the
    searched attribute. For single token queries, this is effectively the same behavior as a partial match operation."""


class CustomerTextFilterDict(TypedDict):
    exact: NotRequired[str | None]
    fuzzy: NotRequired[str | None]
