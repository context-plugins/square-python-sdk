from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CloneOrderRequest(SdkBaseModel):
    """Defines the fields that are included in requests to the `CloneOrder <api-endpoint:Orders-CloneOrder>`__
    endpoint."""

    order_id: str
    """The ID of the order to clone."""

    version: Optional[int] = UNSET
    """An optional order version for concurrency protection.

    If a version is provided, it must match the latest stored version of the order to clone. If a version is not
    provided, the API clones the latest version."""

    idempotency_key: OptionalNullable[str] = UNSET
    """A value you specify that uniquely identifies this clone request.

    If you are unsure whether a particular order was cloned successfully, you can reattempt the call with the same
    idempotency key without worrying about creating duplicate cloned orders. The originally cloned order is returned.

    For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""


class CloneOrderRequestDict(TypedDict):
    order_id: str
    version: NotRequired[int]
    idempotency_key: NotRequired[str | None]
