from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class UpdateItemModifierListsResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    updated_at: Optional[str] = UNSET
    """The database `timestamp
    <https://developer.squareup.com/docs/build-basics/common-data-types/working-with-dates>`__ of this update in RFC
    3339 format, e.g., ``2016-09-04T23:59:33.123Z``."""


class UpdateItemModifierListsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    updated_at: NotRequired[str]
