from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class BatchDeleteCatalogObjectsResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    deleted_object_ids: Optional[list[str]] = UNSET
    """The IDs of all CatalogObjects deleted by this request."""

    deleted_at: Optional[str] = UNSET
    """The database `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ of this deletion
    in RFC 3339 format, e.g., "2016-09-04T23:59:33.123Z"."""


class BatchDeleteCatalogObjectsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    deleted_object_ids: NotRequired[list[str]]
    deleted_at: NotRequired[str]
