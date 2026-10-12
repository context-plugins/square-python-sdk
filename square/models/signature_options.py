from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .signature_image import SignatureImage, SignatureImageDict


class SignatureOptions(SdkBaseModel):
    title: str
    """The title text to display in the signature capture flow on the Terminal."""

    body: str
    """The body text to display in the signature capture flow on the Terminal."""

    signature: Optional[list[SignatureImage]] = UNSET
    """An image representation of the collected signature."""


class SignatureOptionsDict(TypedDict):
    title: str
    body: str
    signature: NotRequired[list[SignatureImageDict]]
