from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class GiftCardActivityBlock(SdkBaseModel):
    """Represents details about a ``BLOCK`` `gift card activity type <entity:GiftCardActivityType>`__."""

    reason: Literal["CHARGEBACK_BLOCK"] = "CHARGEBACK_BLOCK"
    """Indicates the reason for blocking a `gift card <entity:GiftCard>`__."""


class GiftCardActivityBlockDict(TypedDict):
    reason: NotRequired[Literal["CHARGEBACK_BLOCK"]]
