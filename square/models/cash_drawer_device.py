from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CashDrawerDevice(SdkBaseModel):
    id: Optional[str] = UNSET
    """The device Square-issued ID"""

    name: OptionalNullable[str] = UNSET
    """The device merchant-specified name."""


class CashDrawerDeviceDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str | None]
