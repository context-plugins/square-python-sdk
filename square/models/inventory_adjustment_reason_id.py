from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.inventory_adjustment_reason_id_type import InventoryAdjustmentReasonIdTypeOrStr


class InventoryAdjustmentReasonId(SdkBaseModel):
    """Identifies a standard or custom inventory adjustment reason."""

    type_: InventoryAdjustmentReasonIdTypeOrStr = Field(alias="type")
    """The type of inventory adjustment reason.

    Custom reasons use ``CUSTOM`` and include a ``custom_reason_id``. Standard seller-selectable reasons use
    ``RECEIVED``, ``DAMAGED``, ``THEFT``, ``LOST``, ``RETURNED``, ``SPOILAGE_WASTE``, ``SAMPLES_PROMOTIONAL``,
    ``INTERNAL_USE``, ``VENDOR_RETURN``, or ``PRODUCTION_WASTE``.

    The writable standard reasons with direction ``INCREASE`` are ``RECEIVED`` and ``RETURNED``. The writable standard
    reasons with direction ``DECREASE`` are ``DAMAGED``, ``THEFT``, ``LOST``, ``SPOILAGE_WASTE``,
    ``SAMPLES_PROMOTIONAL``, ``INTERNAL_USE``, ``VENDOR_RETURN``, and ``PRODUCTION_WASTE``.

    The ``SALE``, ``RECOUNT``, ``TRANSFER``, ``IN_TRANSIT``, and ``CANCELED_SALE`` values identify system-generated
    inventory events. These values can be returned by Square, but cannot be used when writing inventory adjustments."""

    custom_reason_id: OptionalNullable[str] = UNSET
    """The Square-generated ID of the custom adjustment reason. This field is only set when ``type`` is ``CUSTOM``."""


class InventoryAdjustmentReasonIdDict(TypedDict):
    type_: InventoryAdjustmentReasonIdTypeOrStr
    custom_reason_id: NotRequired[str | None]
