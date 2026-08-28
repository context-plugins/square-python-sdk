from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DeleteSnippetResponse(SdkBaseModel):
    """Represents a ``DeleteSnippet`` response."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class DeleteSnippetResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
