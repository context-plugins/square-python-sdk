from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Site(SdkBaseModel):
    """Represents a Square Online site, which is an online store for a Square seller."""

    id: Optional[str] = UNSET
    """The Square-assigned ID of the site."""

    site_title: OptionalNullable[str] = UNSET
    """The title of the site."""

    domain: OptionalNullable[str] = UNSET
    """The domain of the site (without the protocol). For example, ``mysite1.square.site``."""

    is_published: OptionalNullable[bool] = UNSET
    """Indicates whether the site is published."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the site was created, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp of when the site was last updated, in RFC 3339 format."""


class SiteDict(TypedDict):
    id: NotRequired[str]
    site_title: NotRequired[str | None]
    domain: NotRequired[str | None]
    is_published: NotRequired[bool | None]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
