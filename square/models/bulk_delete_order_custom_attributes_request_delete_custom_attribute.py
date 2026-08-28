from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BulkDeleteOrderCustomAttributesRequestDeleteCustomAttribute(SdkBaseModel):
    """Represents one delete within the bulk operation."""

    key: Optional[str] = UNSET
    """The key of the custom attribute to delete. This key must match the key of an existing custom attribute
    definition."""

    order_id: str
    """The ID of the target `order <entity:Order>`__."""


class BulkDeleteOrderCustomAttributesRequestDeleteCustomAttributeDict(TypedDict):
    key: NotRequired[str]
    order_id: str
