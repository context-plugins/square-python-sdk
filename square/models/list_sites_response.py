from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .site import Site, SiteDict


class ListSitesResponse(SdkBaseModel):
    """Represents a ``ListSites`` response. The response can include either ``sites`` or ``errors``."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    sites: Optional[list[Site]] = UNSET
    """The sites that belong to the seller."""


class ListSitesResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    sites: NotRequired[list[Site | SiteDict]]
