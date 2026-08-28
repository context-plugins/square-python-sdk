from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PublishInvoiceRequest(SdkBaseModel):
    """Describes a ``PublishInvoice`` request."""

    version: int
    """The version of the `invoice <entity:Invoice>`__ to publish. This must match the current version of the invoice;
    otherwise, the request is rejected."""

    idempotency_key: OptionalNullable[str] = UNSET
    """A unique string that identifies the ``PublishInvoice`` request. If you do not provide ``idempotency_key`` (or
    provide an empty string as the value), the endpoint treats each request as independent.

    For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""


class PublishInvoiceRequestDict(TypedDict):
    version: int
    idempotency_key: NotRequired[str | None]
