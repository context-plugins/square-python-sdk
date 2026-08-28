from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.fulfillment_state import FulfillmentStateOrStr
from .enums.fulfillment_type import FulfillmentTypeOrStr


class SearchOrdersFulfillmentFilter(SdkBaseModel):
    """Filter based on `order fulfillment <entity:Fulfillment>`__ information."""

    fulfillment_types: Optional[list[FulfillmentTypeOrStr | None]] = UNSET
    """A list of `fulfillment types <entity:FulfillmentType>`__ to filter for. The list returns orders if any of its
    fulfillments match any of the fulfillment types listed in this field. See `FulfillmentType
    <#type-fulfillmenttype>`__ for possible values"""

    fulfillment_states: Optional[list[FulfillmentStateOrStr | None]] = UNSET
    """A list of `fulfillment states <entity:FulfillmentState>`__ to filter for. The list returns orders if any of its
    fulfillments match any of the fulfillment states listed in this field. See `FulfillmentState
    <#type-fulfillmentstate>`__ for possible values"""


class SearchOrdersFulfillmentFilterDict(TypedDict):
    fulfillment_types: NotRequired[list[FulfillmentTypeOrStr | None]]
    fulfillment_states: NotRequired[list[FulfillmentStateOrStr | None]]
