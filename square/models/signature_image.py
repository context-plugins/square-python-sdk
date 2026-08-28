from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SignatureImage(SdkBaseModel):
    image_type: Optional[str] = UNSET
    """The mime/type of the image data. Use ``image/png;base64`` for png."""

    data: Optional[str] = UNSET
    """The base64 representation of the image."""


class SignatureImageDict(TypedDict):
    image_type: NotRequired[str]
    data: NotRequired[str]
