from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class QrCodeOptions(SdkBaseModel):
    """Fields to describe the action that displays QR-Codes."""

    title: str
    """The title text to display in the QR code flow on the Terminal."""

    body: str
    """The body text to display in the QR code flow on the Terminal."""

    barcode_contents: str
    """The text representation of the data to show in the QR code as UTF8-encoded data."""


class QrCodeOptionsDict(TypedDict):
    title: str
    body: str
    barcode_contents: str
