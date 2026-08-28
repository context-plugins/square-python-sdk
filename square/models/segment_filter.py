from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .filter_value import FilterValue, FilterValueDict


class SegmentFilter(SdkBaseModel):
    """A query filter to search for buyer-accessible appointment segments by."""

    service_variation_id: str
    """The ID of the `CatalogItemVariation <entity:CatalogItemVariation>`__ object representing the service booked in
    this segment."""

    team_member_id_filter: Optional[FilterValue] = UNSET
    """A filter to select resources based on an exact field value. For any given value, the value can only be in one
    property. Depending on the field, either all properties can be set or only a subset will be available.

    Refer to the documentation of the field."""


class SegmentFilterDict(TypedDict):
    service_variation_id: str
    team_member_id_filter: NotRequired[FilterValue | FilterValueDict]
