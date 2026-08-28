from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_version_updated_event_catalog_version import (
    CatalogVersionUpdatedEventCatalogVersion,
    CatalogVersionUpdatedEventCatalogVersionDict,
)


class CatalogVersionUpdatedEventObject(SdkBaseModel):
    catalog_version: Optional[CatalogVersionUpdatedEventCatalogVersion] = UNSET


class CatalogVersionUpdatedEventObjectDict(TypedDict):
    catalog_version: NotRequired[
        CatalogVersionUpdatedEventCatalogVersion | CatalogVersionUpdatedEventCatalogVersionDict
    ]
