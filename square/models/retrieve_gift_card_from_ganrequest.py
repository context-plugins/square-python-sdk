from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RetrieveGiftCardFromGanrequest(SdkBaseModel):
    """A request to retrieve gift cards by their GANs."""

    gan: str
    """The gift card account number (GAN) of the gift card to retrieve. The maximum length of a GAN is 255 digits to
    account for third-party GANs that have been imported. Square-issued gift cards have 16-digit GANs."""


class RetrieveGiftCardFromGanrequestDict(TypedDict):
    gan: str
