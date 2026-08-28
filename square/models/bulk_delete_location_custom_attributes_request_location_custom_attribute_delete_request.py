from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BulkDeleteLocationCustomAttributesRequestLocationCustomAttributeDeleteRequest(SdkBaseModel):
    """Represents an individual delete request in a `BulkDeleteLocationCustomAttributes
    <api-endpoint:LocationCustomAttributes-BulkDeleteLocationCustomAttributes>`__ request. An individual request
    contains an optional ID of the associated custom attribute definition and optional key of the associated custom
    attribute definition."""

    key: Optional[str] = UNSET
    """The key of the associated custom attribute definition. Represented as a qualified key if the requesting app is
    not the definition owner."""


class BulkDeleteLocationCustomAttributesRequestLocationCustomAttributeDeleteRequestDict(TypedDict):
    key: NotRequired[str]
