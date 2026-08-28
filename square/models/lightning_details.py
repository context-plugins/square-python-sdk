from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class LightningDetails(SdkBaseModel):
    """Additional details about ``WALLET`` type payments with the ``brand`` of ``LIGHTNING``."""

    payment_url: OptionalNullable[str] = UNSET
    """Payment URL for the lightning payment, a.k.a. the invoice."""


class LightningDetailsDict(TypedDict):
    payment_url: NotRequired[str | None]
