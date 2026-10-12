from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .snippet import Snippet, SnippetDict


class UpsertSnippetRequest(SdkBaseModel):
    """Represents an ``UpsertSnippet`` request."""

    snippet: Snippet
    """Represents the snippet that is added to a Square Online site. The snippet code is injected into the ``head``
    element of all pages on the site, except for checkout pages."""


class UpsertSnippetRequestDict(TypedDict):
    snippet: SnippetDict
