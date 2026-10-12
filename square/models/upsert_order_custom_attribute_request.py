from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .custom_attribute import CustomAttribute, CustomAttributeDict


class UpsertOrderCustomAttributeRequest(SdkBaseModel):
    """Represents an upsert request for an order custom attribute."""

    custom_attribute: CustomAttribute
    """A custom attribute value. Each custom attribute value has a corresponding ``CustomAttributeDefinition``
    object."""

    idempotency_key: OptionalNullable[str] = UNSET
    """A unique identifier for this request, used to ensure idempotency. For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""


class UpsertOrderCustomAttributeRequestDict(TypedDict):
    custom_attribute: CustomAttributeDict
    idempotency_key: NotRequired[str | None]
