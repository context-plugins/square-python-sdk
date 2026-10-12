from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .custom_attribute import CustomAttribute, CustomAttributeDict


class BulkUpsertLocationCustomAttributesRequestLocationCustomAttributeUpsertRequest(SdkBaseModel):
    """Represents an individual upsert request in a `BulkUpsertLocationCustomAttributes
    <api-endpoint:LocationCustomAttributes-BulkUpsertLocationCustomAttributes>`__ request. An individual request
    contains a location ID, the custom attribute to create or update, and an optional idempotency key."""

    location_id: str
    """The ID of the target `location <entity:Location>`__."""

    custom_attribute: CustomAttribute
    """A custom attribute value. Each custom attribute value has a corresponding ``CustomAttributeDefinition``
    object."""

    idempotency_key: OptionalNullable[str] = UNSET
    """A unique identifier for this individual upsert request, used to ensure idempotency. For more information, see
    `Idempotency <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""


class BulkUpsertLocationCustomAttributesRequestLocationCustomAttributeUpsertRequestDict(TypedDict):
    location_id: str
    custom_attribute: CustomAttributeDict
    idempotency_key: NotRequired[str | None]
