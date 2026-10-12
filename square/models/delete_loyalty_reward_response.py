from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DeleteLoyaltyRewardResponse(SdkBaseModel):
    """A response returned by the API call."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class DeleteLoyaltyRewardResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
