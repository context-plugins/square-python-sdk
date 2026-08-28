from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LoyaltyEventLocationFilter(SdkBaseModel):
    """Filter events by location."""

    location_ids: list[str]
    """The `location <entity:Location>`__ IDs for loyalty events to query. If multiple values are specified, the
    endpoint uses a logical OR to combine them."""


class LoyaltyEventLocationFilterDict(TypedDict):
    location_ids: list[str]
