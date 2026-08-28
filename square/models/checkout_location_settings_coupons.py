from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CheckoutLocationSettingsCoupons(SdkBaseModel):
    enabled: OptionalNullable[bool] = UNSET
    """Indicates whether coupons are enabled for this location."""


class CheckoutLocationSettingsCouponsDict(TypedDict):
    enabled: NotRequired[bool | None]
