from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .inventory_change import InventoryChange, InventoryChangeDict


class BatchChangeInventoryRequest(SdkBaseModel):
    idempotency_key: str
    """A client-supplied, universally unique identifier (UUID) for the request.

    See `Idempotency <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__ in the `API
    Development 101 <https://developer.squareup.com/docs/buildbasics>`__ section for more information."""

    changes: OptionalNullable[list[InventoryChange]] = UNSET
    """The set of physical counts and inventory adjustments to be made. Changes are applied based on the client-supplied
    timestamp and may be sent out of order."""

    ignore_unchanged_counts: OptionalNullable[bool] = UNSET
    """Indicates whether the current physical count should be ignored if the quantity is unchanged since the last
    physical count. Default: ``true``."""


class BatchChangeInventoryRequestDict(TypedDict):
    idempotency_key: str
    changes: NotRequired[list[InventoryChangeDict] | None]
    ignore_unchanged_counts: NotRequired[bool | None]
