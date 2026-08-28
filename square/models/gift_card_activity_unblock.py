from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class GiftCardActivityUnblock(SdkBaseModel):
    """Represents details about an ``UNBLOCK`` `gift card activity type <entity:GiftCardActivityType>`__."""

    reason: Literal["CHARGEBACK_UNBLOCK"] = "CHARGEBACK_UNBLOCK"
    """Indicates the reason for unblocking a `gift card <entity:GiftCard>`__."""


class GiftCardActivityUnblockDict(TypedDict):
    reason: NotRequired[Literal["CHARGEBACK_UNBLOCK"]]
