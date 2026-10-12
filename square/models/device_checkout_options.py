from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .tip_settings import TipSettings, TipSettingsDict


class DeviceCheckoutOptions(SdkBaseModel):
    device_id: str
    """The unique ID of the device intended for this ``TerminalCheckout``. A list of ``DeviceCode`` objects can be
    retrieved from the /v2/devices/codes endpoint. Match a ``DeviceCode.device_id`` value with ``device_id`` to get the
    associated device code."""

    skip_receipt_screen: OptionalNullable[bool] = UNSET
    """Instructs the device to skip the receipt screen. Defaults to false."""

    collect_signature: OptionalNullable[bool] = UNSET
    """Indicates that signature collection is desired during checkout. Defaults to false."""

    tip_settings: Optional[TipSettings] = UNSET
    show_itemized_cart: OptionalNullable[bool] = UNSET
    """Show the itemization screen prior to taking a payment. This field is only meaningful when the checkout includes
    an order ID. Defaults to true."""

    allow_auto_card_surcharge: OptionalNullable[bool] = UNSET
    """Controls whether the mobile client applies Auto Card Surcharge (ACS) during checkout. If true, ACS is applied
    based on Dashboard configuration. If false, ACS is not applied regardless of that configuration. For more
    information, see `Add a Card Surcharge
    <https://developer.squareup.com/docs/terminal-api/additional-payment-checkout-features#add-a-card-surcharge>`__."""


class DeviceCheckoutOptionsDict(TypedDict):
    device_id: str
    skip_receipt_screen: NotRequired[bool | None]
    collect_signature: NotRequired[bool | None]
    tip_settings: NotRequired[TipSettingsDict]
    show_itemized_cart: NotRequired[bool | None]
    allow_auto_card_surcharge: NotRequired[bool | None]
