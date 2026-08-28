from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Snippet(SdkBaseModel):
    """Represents the snippet that is added to a Square Online site. The snippet code is injected into the ``head``
    element of all pages on the site, except for checkout pages."""

    id: Optional[str] = UNSET
    """The Square-assigned ID for the snippet."""

    site_id: Optional[str] = UNSET
    """The ID of the site that contains the snippet."""

    content: str
    """The snippet code, which can contain valid HTML, JavaScript, or both."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the snippet was initially added to the site, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp of when the snippet was last updated on the site, in RFC 3339 format."""


class SnippetDict(TypedDict):
    id: NotRequired[str]
    site_id: NotRequired[str]
    content: str
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
