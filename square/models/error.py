from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.error_category import ErrorCategoryOrStr
from .enums.error_code import ErrorCodeOrStr


class Error(SdkBaseModel):
    """Represents an error encountered during a request to the Connect API.

    See `Handling errors <https://developer.squareup.com/docs/build-basics/handling-errors>`__ for more information."""

    category: ErrorCategoryOrStr
    """Indicates which high-level category of error has occurred during a request to the Connect API."""

    code: ErrorCodeOrStr
    """Indicates the specific error that occurred during a request to a Square API."""

    detail: Optional[str] = UNSET
    """A human-readable description of the error for debugging purposes."""

    field: Optional[str] = UNSET
    """The name of the field provided in the original request (if any) that the error pertains to."""


class ErrorDict(TypedDict):
    category: ErrorCategoryOrStr
    code: ErrorCodeOrStr
    detail: NotRequired[str]
    field: NotRequired[str]
