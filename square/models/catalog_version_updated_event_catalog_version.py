from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CatalogVersionUpdatedEventCatalogVersion(SdkBaseModel):
    updated_at: Optional[str] = UNSET
    """Last modification timestamp in RFC 3339 format."""


class CatalogVersionUpdatedEventCatalogVersionDict(TypedDict):
    updated_at: NotRequired[str]
