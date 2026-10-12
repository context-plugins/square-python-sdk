from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class RevokeTokenResponse(SdkBaseModel):
    success: Optional[bool] = UNSET
    """If the request is successful, this is ``true``."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class RevokeTokenResponseDict(TypedDict):
    success: NotRequired[bool]
    errors: NotRequired[list[ErrorDict]]
