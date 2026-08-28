from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UpdateCatalogImageRequest(SdkBaseModel):
    idempotency_key: str
    """A unique string that identifies this UpdateCatalogImage request. Keys can be any valid string but must be unique
    for every UpdateCatalogImage request.

    See `Idempotency keys <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__ for more
    information."""


class UpdateCatalogImageRequestDict(TypedDict):
    idempotency_key: str
