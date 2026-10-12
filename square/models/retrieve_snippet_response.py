from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .snippet import Snippet, SnippetDict


class RetrieveSnippetResponse(SdkBaseModel):
    """Represents a ``RetrieveSnippet`` response. The response can include either ``snippet`` or ``errors``."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    snippet: Optional[Snippet] = UNSET
    """Represents the snippet that is added to a Square Online site. The snippet code is injected into the ``head``
    element of all pages on the site, except for checkout pages."""


class RetrieveSnippetResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    snippet: NotRequired[SnippetDict]
