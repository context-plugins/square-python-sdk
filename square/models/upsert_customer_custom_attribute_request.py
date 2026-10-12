from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .custom_attribute import CustomAttribute, CustomAttributeDict


class UpsertCustomerCustomAttributeRequest(SdkBaseModel):
    """Represents an `UpsertCustomerCustomAttribute
    <api-endpoint:CustomerCustomAttributes-UpsertCustomerCustomAttribute>`__ request."""

    custom_attribute: CustomAttribute
    """A custom attribute value. Each custom attribute value has a corresponding ``CustomAttributeDefinition``
    object."""

    idempotency_key: OptionalNullable[str] = UNSET
    """A unique identifier for this request, used to ensure idempotency. For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""


class UpsertCustomerCustomAttributeRequestDict(TypedDict):
    custom_attribute: CustomAttributeDict
    idempotency_key: NotRequired[str | None]
