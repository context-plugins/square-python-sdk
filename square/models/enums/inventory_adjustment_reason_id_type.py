from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InventoryAdjustmentReasonIdType(str, Enum):
    """The type of inventory adjustment reason.

    Custom reasons use ``CUSTOM`` and include a ``custom_reason_id``. Standard seller-selectable reasons use
    ``RECEIVED``, ``DAMAGED``, ``THEFT``, ``LOST``, ``RETURNED``, ``SPOILAGE_WASTE``, ``SAMPLES_PROMOTIONAL``,
    ``INTERNAL_USE``, ``VENDOR_RETURN``, or ``PRODUCTION_WASTE``.

    The writable standard reasons with direction ``INCREASE`` are ``RECEIVED`` and ``RETURNED``. The writable standard
    reasons with direction ``DECREASE`` are ``DAMAGED``, ``THEFT``, ``LOST``, ``SPOILAGE_WASTE``,
    ``SAMPLES_PROMOTIONAL``, ``INTERNAL_USE``, ``VENDOR_RETURN``, and ``PRODUCTION_WASTE``.

    The ``SALE``, ``RECOUNT``, ``TRANSFER``, ``IN_TRANSIT``, and ``CANCELED_SALE`` values identify system-generated
    inventory events. These values can be returned by Square, but cannot be used when writing inventory adjustments."""

    RECEIVED = "RECEIVED"
    DAMAGED = "DAMAGED"
    THEFT = "THEFT"
    LOST = "LOST"
    RETURNED = "RETURNED"
    SPOILAGE_WASTE = "SPOILAGE_WASTE"
    SAMPLES_PROMOTIONAL = "SAMPLES_PROMOTIONAL"
    INTERNAL_USE = "INTERNAL_USE"
    VENDOR_RETURN = "VENDOR_RETURN"
    PRODUCTION_WASTE = "PRODUCTION_WASTE"
    SALE = "SALE"
    RECOUNT = "RECOUNT"
    TRANSFER = "TRANSFER"
    IN_TRANSIT = "IN_TRANSIT"
    CANCELED_SALE = "CANCELED_SALE"
    CUSTOM = "CUSTOM"

    __str__ = str.__str__


InventoryAdjustmentReasonIdTypeOrStr: TypeAlias = Annotated[
    InventoryAdjustmentReasonIdType | str, open_enum_validator(InventoryAdjustmentReasonIdType)
]
