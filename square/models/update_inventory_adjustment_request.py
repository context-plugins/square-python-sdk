from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .inventory_adjustment import InventoryAdjustment, InventoryAdjustmentDict


class UpdateInventoryAdjustmentRequest(SdkBaseModel):
    idempotency_key: str
    """A client-supplied, universally unique identifier (UUID) for the request.

    See `Idempotency <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__ in the `Build
    Basics <https://developer.squareup.com/docs/buildbasics>`__ section for more information."""

    adjustment: InventoryAdjustment
    """Represents a change in state or quantity of product inventory at a particular time and location."""


class UpdateInventoryAdjustmentRequestDict(TypedDict):
    idempotency_key: str
    adjustment: InventoryAdjustment | InventoryAdjustmentDict
