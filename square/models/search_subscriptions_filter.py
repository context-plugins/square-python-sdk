from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class SearchSubscriptionsFilter(SdkBaseModel):
    """Represents a set of query expressions (filters) to narrow the scope of targeted subscriptions returned by the
    `SearchSubscriptions <api-endpoint:Subscriptions-SearchSubscriptions>`__ endpoint."""

    customer_ids: OptionalNullable[list[str]] = UNSET
    """A filter to select subscriptions based on the subscribing customer IDs."""

    location_ids: OptionalNullable[list[str]] = UNSET
    """A filter to select subscriptions based on the location."""

    source_names: OptionalNullable[list[str]] = UNSET
    """A filter to select subscriptions based on the source application."""


class SearchSubscriptionsFilterDict(TypedDict):
    customer_ids: NotRequired[list[str] | None]
    location_ids: NotRequired[list[str] | None]
    source_names: NotRequired[list[str] | None]
