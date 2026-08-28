from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ReceiptOptions(SdkBaseModel):
    """Describes receipt action fields."""

    payment_id: str
    """The reference to the Square payment ID for the receipt."""

    print_only: OptionalNullable[bool] = UNSET
    """Instructs the device to print the receipt without displaying the receipt selection screen. Requires
    ``printer_enabled`` set to true. Defaults to false."""

    is_duplicate: OptionalNullable[bool] = UNSET
    """Identify the receipt as a reprint rather than an original receipt. Defaults to false."""


class ReceiptOptionsDict(TypedDict):
    payment_id: str
    print_only: NotRequired[bool | None]
    is_duplicate: NotRequired[bool | None]
